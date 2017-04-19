class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find the minimual price 
        # find the max profit currently 
        if len(prices) <2:
            return 0
            
        minprice = prices[0]
        maxprofit = 0 
        for i in range(1,len(prices)):
            minprice = min(minprice,prices[i])
            profit = prices[i] - minprice
            maxprofit = max(maxprofit,profit)
        return maxprofit