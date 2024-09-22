from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> Node:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        if self.head == data:
            self.head = self.head.next
            return

        previous_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                previous_node.next = current_node.next
                current_node = None
                return
            previous_node = current_node
            current_node = current_node.next

    def reverse_iterative(self) -> Node:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def reverse_recursive(self) -> Node:
        def _reverse_recursive(current_node: Node | None, previous_node: Node | None):
            if not current_node:
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> Node:
        def _reverse_even(
            head: Optional[Node], previous_node: Optional[Node]
        ) -> Optional[Node]:
            if head is None:
                return None
            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)


if __name__ == "__main__":
    l = LinkedList()
    # l.append(7)
    l.append(2)
    l.append(4)
    l.append(6)
    l.append(1)
    l.append(3)
    l.append(2)
    l.append(4)
    l.append(4)
    l.append(6)
    l.print()
    print("########")
    l.reverse_even()
    l.print()

    # l.remove(2)
    # l.remove(8)
    # l.print()
