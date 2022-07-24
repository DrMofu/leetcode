class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_have = [1]*n
        max_len = 1
        for i,curr_num in enumerate(nums):
            lenth = 1
            for j in range(i):
                prev_num = nums[j]
                if prev_num<curr_num:
                    lenth = max(lenth,1+dp_have[j])
            dp_have[i]=lenth
            max_len = max(max_len,lenth)
        return max_len
                    