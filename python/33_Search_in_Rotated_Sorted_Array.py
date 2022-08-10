class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first_num = nums[0]
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (right-left)//2+left
            value = nums[mid]
            if value == target:
                return mid
            if value>=first_num: # mid in the left area
                if first_num<=target<value:
                    right=mid-1
                else:
                    left=mid+1
            else: # mid in the right area
                if value<target<first_num:
                    left=mid+1
                else:
                    right = mid-1
        return -1
                    