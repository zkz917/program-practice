class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
            
            
        start, end = 1, x
        
        while start + 1 < end:
            mid = start + (end - start)/2
            if mid**2 == x:
                return mid 
            elif mid**2 < x:
                start = mid
            else:
                end = mid 
        
        if end**2 == x:
            return end
        else:
            return start 
