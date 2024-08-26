class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        max_profit = 0
        min_price = 1e4
        for price in prices:
            if (price<min_price):
                min_price = price
            elif (price-min_price > max_profit):
                max_profit = price - min_price
        return max_profit
            
        
        
