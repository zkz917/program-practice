### subsets

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        Solution.ret = []
        self.dfs(nums,0,[])
        return Solution.ret
        
    def dfs(self,nums,start,temp):
        Solution.ret.append(temp)
        for i in range(start,len(nums)):
            self.dfs(nums,i+1,temp + [nums[i]])
```

### subsets II with duplicate

```python
class Solution(object):
    def subsetsWithDup(self, candidates):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.ret = []
        candidates.sort()
        self.dfs(0,candidates,[])
        return Solution.ret
        
    def dfs(self,start,candidates,temp):
        
        Solution.ret.append(temp)
        for i in range(start,len(candidates)):
           
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.dfs(i+1,candidates, temp+[candidates[i]])
```

### Permutations 
 
```python

class Solution(object):
    def permute(self, candidates):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.ret = []
        candidates.sort()
        self.dfs(0,candidates,len(candidates),[])
        return Solution.ret
        
    def dfs(self,start,candidates,target,temp):
        if target == 0:
            Solution.ret.append(temp)
            return
        for i in range(0,len(candidates)):
            if candidates[i] in temp:
                continue
            self.dfs(i,candidates,target - 1, temp+[candidates[i]])
```

### Permutations II with duplicate

```python
class Solution(object):
    def permuteUnique(self, candidates):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.ret = []
        Solution.used = [False]*len(candidates)
        candidates.sort()
        self.dfs(0,candidates,0,[])
        return Solution.ret
        
    def dfs(self,start,candidates,target,temp):
        if target == len(candidates):
            Solution.ret.append(temp)
            return
        for i in range(0,len(candidates)):
            # if candidates[i] in temp:
            if Solution.used[i]:
                continue
            if i > 0 and candidates[i] == candidates[i-1] and not Solution.used[i-1]:
                continue
            Solution.used[i] = True
            self.dfs(i,candidates,target + 1, temp+[candidates[i]])
            Solution.used[i] = False
```

### combinations 
```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(1,n,k,[])
        return self.res
        
    def helper(self,start,n,k,temp):
        if k == 0:
            self.res.append(temp)
            return 
        for i in range(start,n+1):
            self.helper(i+1,n,k-1, temp + [i])
```

### Combination sum II
```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        Solution.ret = []
        candidates.sort()
        self.dfs(0,candidates,target,[])
        return Solution.ret
        
    def dfs(self,start,candidates,target,temp):
        if target == 0:
            Solution.ret.append(temp)
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.dfs(i+1,candidates,target - candidates[i], temp+[candidates[i]])
```

### Combination sum III
```python 
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        Solution.ret = []
        candidates = range(1,10)
        self.dfs(0,k,n,candidates,[])
        return Solution.ret
        
    def dfs(self,start,k,n,candidates,temp):
        if n == 0 and k == 0:
            Solution.ret.append(temp)
        for i in range(start,len(candidates)):
            if candidates[i] > n:
                return
            self.dfs(i+1,k-1,n-candidates[i],candidates,temp + [candidates[i]])
```
