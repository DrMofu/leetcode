class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        hold_dp = [0]*n
        sell_dp = [0]*n # can't buy next day
        cooldown = [0]*n # can buy
        hold_dp[0] = -prices[0]
        
        for i in range(1,n):
            price = prices[i]
            hold_dp[i] = max(hold_dp[i-1],cooldown[i-1]-prices[i])
            sell_dp[i] = max(sell_dp[i],hold_dp[i-1]+prices[i])
            cooldown[i] = max(sell_dp[i-1],cooldown[i-1])
            
        return max(sell_dp[-1],cooldown[-1])