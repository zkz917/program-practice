class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		# super(ListNode, self).__init__()
		self.val = x
		self.next = None 

# class solution(object):
# 	def addtwonumber(self,l1,l2):
# 		# l1 listnode 
# 		# l2 listnode 
# 		# return listnode 


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        use stack to remember the leaset important number 
        bottom up 
        """
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        sum =0 
        res = ListNode(0)
        while stack1 or stack2:
            if stack1: 
                sum += stack1.pop(-1)
            if stack2:
                sum += stack2.pop(-1)
            res.val = sum % 10
            head = ListNode(sum // 10)
            head.next = res
            res = head
            sum /=10 
            
        return res.next if res.val == 0 else res
        