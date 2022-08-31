class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_num = -float("inf")
        left=0
        k = 0
        for right, right_num in enumerate(nums):
            if right_num == prev_num:
                nums[right] = "_"
            else:
                nums[left] = right_num
                left+=1
                k+=1
            prev_num = right_num
        
        return k