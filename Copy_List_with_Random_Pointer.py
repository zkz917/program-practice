# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        listmap = dict()
        dummy = head
        
        if not head:
        	return None

        while head:
        	listmap[head] = RandomListNode(head.label)
        	head = head.next
        for node in listmap.keys():
            if node.random:
        	    listmap[node].random = listmap[node.random]
            if node.next:
        	    listmap[node].next = listmap[node.next]

        return listmap[dummy]