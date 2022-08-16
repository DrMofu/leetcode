class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 0
        n = len(nums)
        for i in range(1,n+1):
            missing ^=i
        for num in nums:
            missing ^=num
        return missing
        