class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        maxval = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxval += prices[i] - prices[i-1]
        return maxval
