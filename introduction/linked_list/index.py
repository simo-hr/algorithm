from __future__ import annotations
from typing import Any


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

        previous_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                previous_node.next = current_node.next
                current_node = None
                break
            else:
                previous_node = current_node
                current_node = current_node.next


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    l.remove(2)
    l.remove(8)
    print("#############")
    l.print()
