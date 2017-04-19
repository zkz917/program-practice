# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head1 = None
        while head:
            temp = head.next
            head.next = head1
            head1 = head
            head = temp
            
        return head1
        
