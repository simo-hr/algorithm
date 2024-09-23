from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
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
        new_node.prev = last_node

    def insert(self, data: Any) -> Node:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> Node:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def print_prev(self) -> Node:
        current_node = self.head
        while current_node:
            print(current_node.prev)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                self.head = next_node
                return

        # while current_node and current_node.data != data:
        #     current_node = current_node.next

        # if current_node is None:
        #     return

        # if current_node.next is None:
        #     print("current_node.next is None")
        #     prev = current_node.prev
        #     prev.next = None
        #     return
        # else:
        #     next_node = current_node.next
        #     prev = current_node.prev
        #     prev.next = next_node
        #     next_node.prev = prev
        #     return

        while current_node and current_node.data != data:
            next_node = current_node.next
            if next_node and next_node.data == data:
                current_node.next = next_node.next
                if next_node.next:
                    next_node.next.prev = current_node
                    return
            current_node = current_node.next

    def reverse_iterative(self) -> None:
        prev_node = None
        current_node = self.head
        while current_node:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node

            current_node = current_node.prev
        if prev_node:
            self.head = prev_node.prev

    def reverse_recursive(self) -> None:
        def _reverse_recursive(
            prev_node: Optional[Node], current_node: Optional[Node]
        ) -> None:
            if current_node is None:
                return prev_node
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            return _reverse_recursive(prev_node, current_node.prev)

        prev_node = _reverse_recursive(None, self.head)
        if prev_node:
            self.head = prev_node.prev


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.append(5)
    d.print()
    print("#### reverse_iterative ###")
    d.reverse_iterative()
    d.print()
    print("#### reverse_recursive ###")
    d.reverse_recursive()
    d.print()
    d.print_prev()
