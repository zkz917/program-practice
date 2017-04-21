class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint = 2**31 -1
        minint = -2**31
        
        res = str(abs(x))
        res = int(res[::-1])
        
        if x < 0:
            return -res if -res> minint else 0
        else:
            return res if res < maxint else 0
        
