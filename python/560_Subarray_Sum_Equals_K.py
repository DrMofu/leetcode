class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_hash = {0:1}
        total_sum = 0
        result = 0
        for num in nums:
            total_sum+=num
            if total_sum-k in sum_hash:
                result+=sum_hash[total_sum-k]
            sum_hash[total_sum] = sum_hash.get(total_sum,0)+1
        return result