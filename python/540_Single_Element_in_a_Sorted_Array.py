class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        
        # method 1
        # while left<right:
        #     mid = (left+right)//2
        #     mid = mid//2*2
        #     if nums[mid]==nums[mid+1]:
        #         left = mid+2
        #     else:
        #         right = mid
                
        # method 2
        while left<=right:
            mid = (left+right)//2
            mid = mid//2*2
            if mid==len(nums)-1:
                return nums[mid]
            if nums[mid]==nums[mid+1]:
                left = mid+2
            else:
                right = mid-1
        return nums[left]
            
        