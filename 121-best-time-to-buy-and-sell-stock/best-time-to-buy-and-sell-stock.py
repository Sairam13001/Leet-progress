class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for j in range(1, len(prices)):
            if (prices[j]<min_price):
                min_price = prices[j]
            if (prices[j]-min_price > max_profit):
                max_profit = prices[j] - min_price
        return max_profit
            
        
        
