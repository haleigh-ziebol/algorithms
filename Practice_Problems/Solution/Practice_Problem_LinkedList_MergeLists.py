class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def mergeTwoLists(list1, list2):
    # Initialize a dummy node to start the merged list
    dummy = ListNode()
    current = dummy

    # Traverse through both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining elements, if any
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next
# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Create test linked lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Call the merge function
merged_list = mergeTwoLists(list1, list2)

# Print the merged list
print("Merged List:")
print_linked_list(merged_list)