class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        prev_sum = 0
        for num in nums:
            prev_sum = max(num,prev_sum+num)
            max_sum = max(max_sum,prev_sum)
        return max_sum