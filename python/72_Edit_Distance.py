class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if not m:
            return n
        if not n:
            return m
        
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(n+1):
            dp[0][i]=i
        
        for i in range(m+1):
            dp[i][0]=i
            
        for i,char_a in enumerate(word1):
            for j,char_b in enumerate(word2):
                if char_a==char_b:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1]=min(min(dp[i][j],dp[i+1][j]),dp[i][j+1])+1
        return dp[-1][-1]