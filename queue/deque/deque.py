"""
Python List already have them implemented in it
"""


class Deque:
    def __init__(self, size=0):
        self.size = size  # max size
        self.queue = []

    def addRear(self, item):
        if self.isFull():
            raise Exception('Queue is Full')
        self.queue.append(item)

    def addFront(self, item):
        if self.isFull():
            raise Exception('Queue is Full')

        self.queue.insert(0, item)

    def removeFront(self):
        if self.isEmpty():
            raise Exception('Queue is Empty')
        return self.queue.pop()

    def removeRear(self):
        if self.isEmpty():
            raise Exception('Queue is Empty')
        return self.queue.pop(0)

    def isFull(self):
        return self.size == len(self.queue)

    def isEmpty(self):
        return not len(self.queue)
