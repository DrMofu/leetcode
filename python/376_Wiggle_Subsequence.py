class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # have_dp_up = [1]*n
        # have_dp_down = [1]*n
        # max_len = 0
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             have_dp_up[i] = max(have_dp_up[i],have_dp_down[j]+1)                
        #         if nums[j]>nums[i]:
        #             have_dp_down[i] = max(have_dp_down[i],have_dp_up[j]+1)
        #     max_len = max(max_len,max(have_dp_down[i],have_dp_up[i]))
        # print(have_dp_up,have_dp_down)
        # return max_len

        n = len(nums)
        have_dp_up = [1]*n
        have_dp_down = [1]*n
        max_len = 1
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                have_dp_up[i] = max(have_dp_up[i],have_dp_down[i-1]+1)  
                have_dp_down[i] = have_dp_down[i-1]
            elif nums[i-1]>nums[i]:
                have_dp_down[i] = max(have_dp_down[i],have_dp_up[i-1]+1)
                have_dp_up[i] = have_dp_up[i-1]
            else:
                have_dp_down[i] = have_dp_down[i-1]
                have_dp_up[i] = have_dp_up[i-1]
            max_len = max(max_len,max(have_dp_down[i],have_dp_up[i]))
            
        return max_len