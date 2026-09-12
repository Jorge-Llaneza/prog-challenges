# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #eliminate edge cases
        if not list1 and list2: return list2
        if not list2 and list1: return list1
        if not list1 and not list2: return None

        #decide who is the first node
        if list1.val <= list2.val:
            current = list1
            list1 = list1.next
        else: 
            current = list2
            list2 = list2.next

        start = current

        finished = False

        while not finished:
            if not list1: 
                current.next = list2
                break
            if not list2: 
                current.next = list1
                break

            if list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
            

        return start  


list1 = ListNode(1,ListNode(2, ListNode(4)))
list2 = ListNode(1,ListNode(3, ListNode(4)))

Solution().mergeTwoLists(list1, list2)
            