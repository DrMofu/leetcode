class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # try 1
        # dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        # # amount==0, all zero
        # # coin_id==0, all -1 (except dp[0][0])
        # for i in range(1,amount+1):
        #     dp[0][i]=-1
            
        # for index,coin in enumerate(coins):
        #     index = index+1
        #     for value in range(amount+1):
        #         possible_num = value//coin
        #         min_coin = dp[index-1][value]
        #         for k in range(1,possible_num+1):
        #             if dp[index-1][value-k*coin]==-1:
        #                 continue
        #             if min_coin==-1:
        #                 min_coin=dp[index-1][value-k*coin]+k
        #             else:
        #                 min_coin = min(min_coin,dp[index-1][value-k*coin]+k)
        #         dp[index][value] = min_coin
            
        # return dp[-1][-1]

        # try 2
        # dp = [[-1]*(amount+1) for i in range(len(coins)+1)]
        # for i in range(len(coins)+1):
        #     dp[i][0]=0
            
        # for index,coin in enumerate(coins):
        #     index = index+1
        #     for value in range(1,amount+1):
        #         if value-coin<0:
        #             dp[index][value]=dp[index-1][value]
        #             continue
        #         if dp[index-1][value]!=-1 and dp[index][value-coin]==-1:
        #             dp[index][value] = dp[index-1][value]
        #         elif dp[index-1][value]==-1 and dp[index][value-coin]!=-1:
        #             dp[index][value] = dp[index][value-coin]+1
        #         elif dp[index-1][value]!=-1 and dp[index][value-coin]!=-1:
        #             dp[index][value] = min(dp[index-1][value],dp[index][value-coin]+1)

        dp = [-1]*(amount+1)
        dp[0]=0
            
        for coin in coins:
            for value in range(coin,amount+1):
                if dp[value-coin]==-1:
                    continue
                if dp[value]==-1:
                    dp[value] = dp[value-coin]+1
                else:
                    dp[value] = min(dp[value],dp[value-coin]+1)
            
        return dp[-1]