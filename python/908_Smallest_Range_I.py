class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_value = nums[0]
        min_value = nums[0]
        for num in nums:
            max_value = max(num,max_value)
            min_value = min(num,min_value)
        return max(0,(max_value-min_value)-2*k)
            