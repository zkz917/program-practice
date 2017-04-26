# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head 
            
            
        node_len = 0
        head1 = head
        while head1:
            node_len += 1
            head1 = head1.next
            
        k = k % node_len
        
        slow = fast = head
        #  init two pointers 
        while k > 0:
            fast = fast.next
            k -=1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = head
        temp = slow.next
        slow.next = None
        
        return temp
        
            
