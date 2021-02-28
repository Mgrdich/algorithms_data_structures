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


d = Deque(5)
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
d.addFront(10)
try:
    d.addFront(5)
except:
    print('Full Queue')

try:
    d.addRear(5)
except:
    print('Full Queue')

print(d.isEmpty())
print(d.isFull())
print(d.queue)
d.removeFront()
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.queue)

d.removeRear()
d.removeRear()
d.removeRear()
d.removeRear()
d.removeRear()

print(d.queue)

try:
    d.removeRear()
except:
    print('Empty Queue')

try:
    d.removeFront()
except:
    print('Empty Queue')
