class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtEnd(self, data):
        node = Node(data)

        # empty
        if self.head is None:
            self.head = node
            return

        # find the last
        last = self.head
        while last.next:
            last = last.next

        last.next = node

    @staticmethod
    def insertAfterNode(node, data):
        if node is None:  # todo maybe check node instance
            raise Exception('Not a Valid Node')

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def deletingNode(self, position):
        if self.head is None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None  # free memory
            return

        # find the index to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next

        # if the key is not present
        if temp_node is None:
            return

        # if the key is not present
        if temp_node.next is None:
            return

        # since you arrive one steps before
        nextNode = temp_node.next.next
        temp_node.next = None
        temp_node.next = nextNode
