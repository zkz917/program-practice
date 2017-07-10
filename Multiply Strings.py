class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        d = [0 for i in range(len(num1) + len(num2)) ] 
        for i in range(len(num1)):
            val = int(num1[i])
            for j in range(len(num2)):
                n = val* int(num2[j])
                d[i+j] += n
        for i in range(len(d)):
            digit = d[i] % 10
            carry = d[i] / 10
            if i < len(d) -1:
                d[i+1] += carry 
            res.append(str(digit))
        result = "".join(res)[::-1]
        result = result.lstrip('0')
        if not result:
            return '0'
        else:
            return result 