class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.quickselect(nums,k,0,len(nums)-1)
        
    def quickselect(self,nums,k,start,end):
        if start == end:
            return nums[start]
            
        i, j = start, end
        pivot = nums[(i+j)/2]
        while i <=j:
            while i<=j and nums[i] > pivot:
                i+=1
            while i <=j and nums[j]  < pivot:
                j -=1
            if i <=j:
                nums[i], nums[j] = nums[j], nums[i] 
                i +=1
                j -=1
        
        if start + k -1 <= j:
            self.quickselect(nums,k,start,j)
        if start + k -1 >= i:
            self.quickselect(nums,k-(i-start),i,end)
        return nums[j+1]
