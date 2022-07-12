class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def check(nums):
            if not len(nums):
                return True
            prev = nums[0]
            for num in nums:
                if num<prev:
                    return False
                prev=num
            return True
        
        if not len(nums):
            return True
        prev = nums[0]
        for i,num in enumerate(nums):
            if num<prev:
                return check(nums[:i-1]+nums[i:]) or check(nums[:i]+nums[i+1:])
            prev=num
        return True