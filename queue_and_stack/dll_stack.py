import sys
sys.path.append('../Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()


    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        value = None
        if self.size > 0:
            value = self.storage.remove_from_tail()
            self.size -= 1
        return value

    def len(self):
        return self.size
