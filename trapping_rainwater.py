class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        
        res = 0
        
        leftmax, rightmax = 0,0
        
        while left < right:
            
            leftmax = max(leftmax, height[left])
            
            rightmax = max(rightmax,height[right])
            
            if leftmax < rightmax:
        
                res += leftmax -height[left]
                left +=1
            
            else:
                res += rightmax - height[right]
                right -=1
                
        return res
                
            