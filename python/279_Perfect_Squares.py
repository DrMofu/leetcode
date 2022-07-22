import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(1,n+1):
            min_num = dp[i-1]+1
            for j in range(1,int(math.sqrt(i))+1):
                square =j*j
                if i-square>=0:
                    min_num = min(min_num,dp[i-square]+1)
            dp[i]=min_num
        return dp[-1]