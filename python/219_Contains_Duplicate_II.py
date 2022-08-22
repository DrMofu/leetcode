class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_set = set()
        for i in range(min(k+1,len(nums))):
            num = nums[i]
            if num in hash_set:
                return True
            hash_set.add(num)
        
        for i in range(k+1,len(nums)):
            old_num = nums[i-k-1]
            hash_set.remove(old_num)
            new_num = nums[i]
            if new_num in hash_set:
                return True
            hash_set.add(new_num)
            
        return False