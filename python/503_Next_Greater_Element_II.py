class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1]*n
        stack = []
        for i in range(2*n):
            i = i%n
            num = nums[i]
            while len(stack) and stack[-1][0]<num:
                last_num, last_index = stack.pop(-1)
                result[last_index] = num
            stack.append([num,i])
        return result