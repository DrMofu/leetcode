class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # DP
        # hold_stock = [-prices[0]]
        # no_stock = [0]
        # for price in prices[1:]:
        #     hold_stock_money = max(no_stock[-1]-price,hold_stock[-1])
        #     no_stock_money = max(no_stock[-1],hold_stock[-1]+price)
        #     hold_stock.append(hold_stock_money)
        #     no_stock.append(no_stock_money)
        # return no_stock[-1]
        
        total = 0
        last_price = prices[0]
        for price in prices:
            total+=max(0,price-last_price)
            last_price = price
        return total