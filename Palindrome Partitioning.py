class Solution(object):
    def partition(self, nums):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.ret = []
        self.dfs(nums,0,[])
        return Solution.ret
        
    def dfs(self,nums,start,temp):
        if start == len(nums):
            Solution.ret.append(temp)
        # Solution.ret.append(temp)
        for i in range(start,len(nums)):
            if not self.isp(nums[start:i+1]):
                continue
            self.dfs(nums,i+1,temp + [nums[start:i+1]])
            
    def isp(self,s):
        return s == s[::-1]
    
        
