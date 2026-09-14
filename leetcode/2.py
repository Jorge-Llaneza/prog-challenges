# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #Make sure they contain a value
        if not l1 and not l2 : return [0]
        if not l1 and l2: return l2
        if l1 and not l2: return l1

        current = ListNode((l1.val + l2.val)%10)
        first_node = current
        carry = (l1.val + l2.val) // 10
    
        while True:
            toAdd = carry
            if l1 and l1.next:
                toAdd += l1.next.val
            if l1:
                l1 = l1.next
            if l2 and l2.next:
                toAdd += l2.next.val
            if l2:
                l2 = l2.next

            if not l2 and not l1 and toAdd == 0: 
                return first_node
            else: 
                carry = toAdd // 10
                current.next = ListNode(toAdd%10)
                current = current.next

Solution().addTwoNumbers(ListNode(0, ListNode(8, ListNode(6))), ListNode(6, ListNode(7, ListNode(8))))

