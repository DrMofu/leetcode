class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        dst = len(nums)-1
        for i,num in enumerate(nums):
            max_pos = max(max_pos,i+num)
            if max_pos >= dst:
                return True
            if max_pos==i:
                return False
        return True