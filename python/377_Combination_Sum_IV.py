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
            print(dp)
        
#         # no combination
#         for num in nums:
#             for value in range(1,target+1):
#                 if value-num>=0:
#                     dp[value] += dp[value-num]
#             print(dp)
        
        return dp[-1]