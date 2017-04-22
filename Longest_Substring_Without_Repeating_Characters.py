class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        substr = ""
        maxlen = 0
        if not s:
            return 0
        if len(s)< 2:
            return 1
        
        for i in range(len(s)):
            substr = s[head:i+1]
            
            while self.duplicated(substr):

                head +=1
                substr = s[head:i+1]

                
            
            maxlen = max(maxlen,len(substr))
            
        return maxlen
    
    def duplicated(self,s):
        return len(s) != len(set(s))
#############################################################################
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
