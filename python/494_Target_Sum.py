class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        sum_value = sum(nums)
        W= 2*sum_value+1
        prev_dp = [0]*W
        new_dp = [0]*W
        prev_dp[sum_value]=1
        for num in nums:
            for i in range(W):
                left, right = 0,0
                if i-num>=0:
                    left = prev_dp[i-num]                
                if i+num<W:
                    right = prev_dp[i+num]
                new_dp[i] = left+right
            prev_dp = new_dp
            new_dp = [0]*W
        if sum_value+target>=W or sum_value+target<0:
            return 0
        return prev_dp[sum_value+target]