class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_stock_1 = -prices[0]
        sell_stock_1 = 0
        buy_stock_2 = -prices[0]
        sell_stock_2 = 0
        for price in prices[1:]:
            buy_stock_1 = max(buy_stock_1,-price)
            sell_stock_1 = max(sell_stock_1,buy_stock_1+price)
            buy_stock_2 = max(buy_stock_2,sell_stock_1-price)
            sell_stock_2 = max(sell_stock_2,buy_stock_2+price)
        return sell_stock_2
        