class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         n = len(nums)
#         rob = [0]*(n+1)
#         not_rob = [0]*(n+1)
#         for i in range(n):
#             value = nums[i]
#             rob[i+1]=value+not_rob[i]
#             not_rob[i+1] = max(not_rob[i],rob[i])
#         return max(not_rob[-1],rob[-1])
        
        rob = 0
        not_rob = 0
        for value in nums:
            not_rob,rob = max(not_rob,rob),value+not_rob
        return max(not_rob,rob)
    