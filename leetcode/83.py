# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
    
        left = head

        while left.next is not None:
            right = left.next
            while right.val == left.val:
                if right.next is not None:
                    right = right.next
                else:
                    left.next = None
                    return head
            left.next = right
            left = right
        
        return head

def array_to_linked_list(arr):
    # Handle the empty list case
    if not arr:
        return None
    
    # Initialize a dummy node to start the list
    dummy = ListNode(0)
    current = dummy
    
    # Iterate through the array and create nodes
    for value in arr:
        current.next = ListNode(value)
        current = current.next
        
    # The actual head is dummy.next
    return dummy.next

sorted = Solution().deleteDuplicates(array_to_linked_list([1,1,2,3,3]))
while sorted.next:
    print(sorted.val)
    sorted = sorted.next