class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        if not nums:
            return ret
            
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            if i >0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.append([nums[i],nums[j],nums[k]])
                    while j< k and nums[j] == nums[j+1]:
                        
                        j+=1
                    while j< k and nums[k] == nums[k-1]:
                        
                        k-=1   
                    j+=1
                    k -=1
                   
                elif nums[j] + nums[k] + nums[i] < 0:
                    j +=1
                else: 
                    k -=1
        return ret
                
