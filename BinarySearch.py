class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Palindrome(self):
        f = self
        while self is not None:
            print(self)
            self = self.next




head = Node(1)
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)

