class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # consider it as a 0-1 bagpack problem with sum/2 weights
        n = len(nums)
        total_weight = sum(nums)
        if total_weight%2 !=0:
            return False
        W = total_weight//2
        can_we_fit = [False]*(W+1)
        can_we_fit[0]= True
        for num in nums:
            for i in range(W,0,-1):
                if i-num<0:
                    continue
                can_we_fit[i] = can_we_fit[i]|can_we_fit[i-num]
            # print(can_we_fit)
        return can_we_fit[-1]