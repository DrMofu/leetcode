class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def sub_rob(nums):
            rob = 0
            not_rob = 0
            for value in nums:
                not_rob,rob = max(not_rob,rob),value+not_rob
            return max(not_rob,rob)
        return max(sub_rob(nums[1:]),sub_rob(nums[:-1]))
