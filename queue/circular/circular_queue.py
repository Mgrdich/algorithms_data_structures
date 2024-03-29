"""
Python List already have them implemented in it
"""


class CircularQueue:
    def __init__(self, size=0):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, element):
        if (self.tail + 1) % self.size == self.head:
            raise Exception("The Circular Queue is full")
        elif self.head == -1:  # initial empty case
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = element
        else:
            self.tail = (self.tail + 1) % self.size  # last index modulo thingy
            self.queue[self.tail] = element

    def dequeue(self):
        if self.head == -1:
            raise Exception("The Circular Queue is Empty")
        elif self.head == self.tail:
            temp = self.queue[self.tail]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp


# TODO can be moved to py test files


# remember the pointer is what we care about
queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
queue.dequeue()

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.queue)

try:
    queue.enqueue(44)
except:
    print("Full")

queue1 = CircularQueue(2)

try:
    queue1.dequeue()
except:
    print("Empty")
