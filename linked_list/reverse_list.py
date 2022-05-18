# Given the head of a singly linked list, reverse the list, and return the reversed list.

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
