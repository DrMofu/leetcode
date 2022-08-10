class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        smallest, largest = nums[0],nums[-1]
        ans = largest-smallest
        for i in range(len(nums)-1): # have to use current_num and next_num. Because current_num can't +k and -k at the same time.
            current_num = nums[i]
            next_num = nums[i+1]
            upper_bound = max(largest-k,current_num+k)
            lower_bound = min(smallest+k,next_num-k)
            ans = min(ans,upper_bound-lower_bound)
        return ans