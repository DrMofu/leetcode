class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Time limit exceeded 0(N^2)
        # sum_till_it = [0]*len(nums)
        # counter = 0
        # for i,num in enumerate(nums):
        #     for j in range(i+1):
        #         sum_till_it[j]+=num
        #         if sum_till_it[j]%k==0:
        #             counter+=1
        # return counter
        
        sum_hash = {0:1}
        total_sum = 0
        result = 0
        for num in nums:
            total_sum+=num
            total_sum_mod = total_sum%k
            result+= sum_hash.get(total_sum_mod,0)
            sum_hash[total_sum_mod] = sum_hash.get(total_sum_mod,0)+1
        return result