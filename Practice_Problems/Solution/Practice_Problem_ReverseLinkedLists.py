class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Linking nodes to form the linked list 1->2->3->4->5->NULL
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None  # This is the last node, so it points to None

# The head of the list is the first node
head = node1

def reverseList(head):
    reversed_part = None
    current = head

    while current:
        future = current.next
        current.next = reversed_part
        reversed_part = current
        current = future

    return reversed_part

# Function to print the list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("NULL")

# Print the original list
print("Original List:")
printList(head)

# Reverse the list
reversed_head = reverseList(head)

# Print the reversed list
print("\nReversed List:")
printList(reversed_head)


