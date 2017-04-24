class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations)
        
        clen = len(citations)
        res = 0
        for i in range(clen):
            if citations[i] >= clen:
                return min(citations[i],clen)
            clen -=1
            
        return 0
                
            
