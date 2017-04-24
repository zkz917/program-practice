class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        if not str:
            return 0
        
        maxval = 2**31 - 1
        minval = -2**31
        str = str.strip()
        sign = 0
        sumval = 0 
        if str[0] == '-':
            sign = 1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
            
        for i in str:
            if ord(i) <= ord('9') and ord(i) >= ord('0'):
                v = ord(i)-ord('0')
                sumval = sumval*10 + v
                
                
            else:
                if sumval:
                    break
                else:
                    return 0
                    
        if sign:
            sumval = -sumval
        
        if sumval < minval:
            return minval
        if sumval > maxval:
            return maxval
        
        return sumval
            
