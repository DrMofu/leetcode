class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_id = {}
        for i,num in enumerate(nums):
            other_num = target-num
            if other_num in num_to_id:
                return [num_to_id[other_num],i]
            num_to_id[num]=i
        return [-1,-1]