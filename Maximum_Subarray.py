class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval = sumval = nums[0]
        for i in range(1,len(nums)):
            maxval = max(nums[i],maxval+nums[i])
            sumval = max(sumval,maxval)
        return sumval 
