class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold_stock = -prices[0]-fee
        no_stock = 0
        for price in prices[1:]:
            hold_stock = max(no_stock-price-fee,hold_stock)
            no_stock = max(no_stock,hold_stock+price)
        return no_stock