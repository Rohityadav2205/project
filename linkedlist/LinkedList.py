class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    newnode = ListNode(1)
    newnode.next = ListNode(2)
    newnode.next.next = ListNode(3)
    newnode.next.next.next = ListNode(4)
    newnode.next.next.next.next = ListNode(9)
    # newnode=ListNode(1) command is used to connect or print first node after this you can add  next newnode.next=ListNode(2)
    # you can add many list use this command newnode.next.next=ListNode(3)
    while newnode is not None:
        print(newnode.value)
        newnode = newnode.next
