class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) <2:
            return s
        
        self.lo = 0
        self.maxlen = 0
        
        for i in range(len(s)-1):
            self.extendp(s,i,i)
            self.extendp(s,i,i+1)
        return s[self.lo:self.lo + self.maxlen]
        
    def extendp(self,s,i,j):
        while i >=0 and j < len(s) and s[i] == s[j]:
            i -=1
            j +=1
        if j-i - 1 > self.maxlen:
            self.maxlen = j -i - 1
            self.lo = i+1
