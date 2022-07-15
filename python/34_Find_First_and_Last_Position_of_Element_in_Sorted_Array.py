class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        if not len(nums):
            return [-1,-1]
        # find left bounary:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right= mid
        if left==len(nums) or nums[left]!=target:
            return [-1,-1]
        left_boundary = left
        
        # find right bounary
        # left is still the same
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right=mid-1
            else:
                left= mid+1
        right_boundary = left-1
        return [left_boundary,right_boundary]
            