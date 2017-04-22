class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p1, p2 = 0,1
        # use two pointers to solve the problem 
        while p2 < len(nums):
            if p2 < len(nums) and nums[p1] != nums[p2]:
                # move the pointer one step further 
                p1 +=1
                # swap the numbers 
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p2 +=1
            else:
                p2+=1
        
        return p1+1
            

