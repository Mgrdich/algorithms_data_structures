"""
Python List already have them implemented in it
"""


class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, element):
        if len(self.queue) == self.size:
            raise Exception('Queue is Full')

        self.queue.append(element)

    def dequeue(self):
        if not len(self.queue):
            return None

        return self.queue.pop(0)

    def isEmpty(self):
        return not len(self.queue)

    def isFull(self):
        return len(self.queue) == self.size

    def peek(self):
        if not len(self.queue):
            return None
        return self.queue[0]



