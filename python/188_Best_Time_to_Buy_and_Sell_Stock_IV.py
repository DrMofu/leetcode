class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        buy_records = [-prices[0]]*(k+1)
        sell_records = [0]*(k+1)
        for price in prices[1:]:
            for i in range(1,k+1):
                buy_records[i] = max(buy_records[i],sell_records[i-1]-price)
                sell_records[i] = max(sell_records[i],buy_records[i]+price)
            # print(buy_records,sell_records)
        return sell_records[-1]