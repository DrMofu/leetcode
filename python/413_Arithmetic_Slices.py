class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # if n<3:
        #     return 0
        # right=2
        # diff = nums[1]-nums[0]
        # while right<n and nums[right]-nums[right-1]==diff:
        #     right+=1
        # current_sub_num = int((right-1)*(right-2)/2)
        # return current_sub_num + self.numberOfArithmeticSlices(nums[right-1:])
        n = len(nums)
        dp = [0]*n
        for i in range(2,n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
                
        total = 0
        for value in dp:
            total+=value
        return total
            
        