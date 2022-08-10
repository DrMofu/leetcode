class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        n = len(nums)
        for first in range(n):
            if first and nums[first]==nums[first-1]: # ignore it, we already considered it
                continue
            target = -nums[first]
            third = n-1            
            for second in range(first+1,n):
                if second>first+1 and nums[second]==nums[second-1]: # ignore it, we already considered it
                    continue
                while second<third and nums[second]+nums[third]>target:
                    third-=1
                if second==third:
                    break
                if nums[second]+nums[third]==target:
                    results.append([nums[first],nums[second],nums[third]])
        return results