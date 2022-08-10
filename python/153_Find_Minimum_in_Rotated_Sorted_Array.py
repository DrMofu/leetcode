class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums[-1]>=nums[0]:
        #     return nums[0]
        left = 0
        right = len(nums)-1
        last_one = nums[-1]
        while left<right:
            mid = (left+right)//2
            if nums[mid]>last_one: # in the right area
                left = mid+1
            else: # in the left area
                right = mid
        return nums[left]