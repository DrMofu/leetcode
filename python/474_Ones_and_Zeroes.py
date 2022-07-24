class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(m+1)]
        max_num =0
        for string in strs:
            zero_num = 0
            one_num = 0
            for char in string:
                if char=="1":
                    one_num += 1
                if char=="0":
                    zero_num += 1
            for i in range(m,zero_num-1,-1):
                for j in range(n,one_num-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zero_num][j-one_num]+1)
                    max_num = max(max_num,dp[i][j])
                    
        return max_num
            