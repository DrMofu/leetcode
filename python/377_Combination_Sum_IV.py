class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0]=1
            
        for value in range(1,target+1):
            for num in nums:
                if value-num>=0:
                    dp[value] += dp[value-num]
        return dp[-1]