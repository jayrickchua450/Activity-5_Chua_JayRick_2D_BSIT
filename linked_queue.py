# Queue implementation using a linked list with front and rear references.

from node import Node

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity; it can fill only if memory runs out.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element.")
        return self.front.value

    def __str__(self):
        values = []
        current = self.front
        while current is not None:
            values.append(current.value)
            current = current.next
        if not values:
            return "Queue: empty"
        return "Queue (front to rear): " + str(values)
