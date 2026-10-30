# Stack implementation using a singly linked list.
# Push and pop happen at the head/top, so both are O(1).

from node import Node

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity; it can fill only if memory runs out.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element.")
        return self.top.value

    def __str__(self):
        values = []
        current = self.top
        while current is not None:
            values.append(current.value)
            current = current.next
        if not values:
            return "Stack: empty"
        return "Stack (top to bottom): " + str(values)
