class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def addfirst(self, value):
        newnode = ListNode(value)
        newnode.next = self.head
        self.head = newnode

    def __len__(self):
        n = 0
        start = head.head
        while start is not None:
            n += 1
            start = start.next
        return n

    def traverse(self):
        start = head.head
        while start is not None:
            print(start.value, end=',')
            start = start.next
        print()

    def find(self, value):
        start = head.head
        while start is not None:
            if start.value == value:
                return True
            start = start.next
        return False


if __name__ == '__main__':
    head = LinkedList()
    for i in range(3, 9):
        head.addfirst(i)
    head.traverse()
    print(head.find(7))
    print(head.find(-7))
    print(len(head))
