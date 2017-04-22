class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        freq = [0]*26
        adict = dict()
        for w in strs:
            freq = [0]*26
            for i in w:
                freq[ord(i)-ord('a')]+=1
            key = "".join(str(e) for e in freq)
            if key not in adict:
                adict[key] = [w]
            else:
                adict[key].append(w)
        return adict.values()
                
