class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        _sum = 0
        self.dp = [_sum]
        for num in nums:
            _sum+=num
            self.dp.append(_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.dp[right+1]-self.dp[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)