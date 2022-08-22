class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        while left<=right:
            mid = (right-left)//2+left
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right = mid-1
            else:
                left=mid+1
                
        # right: the pos smaller than target
        # left: the pos larger than target
        return left
            