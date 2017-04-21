class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumdit = {}
        for i in range(len(nums)):
            if target - nums[i] in sumdit:
                return [i,sumdit[target-nums[i]]]
            else:
                sumdit[nums[i]] = i
        return None
                
        
