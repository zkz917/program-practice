# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy = head
        sumval = 0
        
        while l1 or l2:
            if l1:
                sumval += l1.val
                l1 = l1.next
            if l2: 
                sumval += l2.val
                l2 = l2.next
            head.next = ListNode(sumval % 10)
            head = head.next
            sumval /= 10
        
        if sumval:
            head.next = ListNode(sumval)
        
        return dummy.next
