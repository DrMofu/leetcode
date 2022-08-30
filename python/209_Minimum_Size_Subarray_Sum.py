class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_len = n+1
        left = 0
        curr_val = 0
        for right in range(n):
            curr_val += nums[right]
            # find left boundary
            while left<n and curr_val>=target:
                min_len = min(min_len,(right-left+1))
                curr_val -= nums[left]
                left+=1
            
        return min_len if min_len<=n else 0