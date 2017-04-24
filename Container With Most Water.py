class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        left, right = 0, len(height)-1
        maxval = 0
        while left < right:
            if height[left] < height[right]:
                maxval = max(maxval,(right-left)*height[left])
                left +=1
                
            else:
                maxval = max(maxval,(right-left)*height[right])
                right -=1
        return maxval
        
        
