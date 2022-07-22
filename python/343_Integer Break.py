class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[1]=1
        for i in range(1,n+1):
            max_product = 1
            for j in range(1,i):
                max_product = max(max_product,max(dp[j]*(i-j),j*(i-j)))
            dp[i]=max_product
        return dp[-1]