class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pairs.sort(key=lambda x:x[0])
        # n = len(pairs)
        # have_dp = [1]*n
        # max_len = 0
        # for i in range(n):
        #     for j in range(i):
        #         if pairs[j][1]<pairs[i][0]:
        #             have_dp[i] = max(have_dp[i],have_dp[j]+1)
        #     max_len = max(max_len,have_dp[i])
        # return max_len
        
        # greedy: select the first finished one
        pairs.sort(key=lambda x:x[1])
        current = float("-inf")
        ans = 0
        for x,y in pairs:
            if current<x:
                current = y
                ans += 1
        return ans
                
            