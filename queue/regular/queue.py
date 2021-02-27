"""
Python List already have them implemented in it
"""


class Queue:
    def __init__(self, size=0):
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


que = Queue(3)
print(que.isEmpty())

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
try:
    que.enqueue(5)
except:
    print('Full Queue')

print(que.peek())
print(que.isFull())
print(que.dequeue())
que.dequeue()
que.dequeue()
que.dequeue()

print(que.queue)
