class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        #  use two pointers if the 
        while i < len(nums):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
                i+=1
            else:
                i+=1
            