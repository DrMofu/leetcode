class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value_count ={}
        for num in nums:
            value_count[num] = value_count.get(num,0)+1
        
        max_len = 0
        for key in value_count:
            if key+1 in value_count:
                max_len = max(max_len,value_count[key]+value_count[key+1])
        return max_len