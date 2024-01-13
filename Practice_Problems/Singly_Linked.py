## reverse singly linked list in place

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    reversed_part = None
    current = head
    while current:
        future = current.next
        current.next = reversed_part
        reversed_part = current
        current = future
    return reversed_part