class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        tmp = []
        n = len(nums)
        added = [False]*n
        
        def backtrack(index):
            # end state
            if index==n:
                ans.append(tmp[:])
                return           
          
                  
            backtrack(index+1)
            if index>0 and nums[index-1]==nums[index] and not added[index-1]:
                return
            
            tmp.append(nums[index])
            added[index]=True            
            backtrack(index+1)            
            tmp.pop(-1)           
            added[index]=False  
            
                
        backtrack(0)
        return ans