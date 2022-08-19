class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        tmp = []
        n = len(nums)
        
        def backtrack(index):
            # end state
            if index==n:
                ans.append(tmp[:])
                return           
          
                  
            backtrack(index+1)
            tmp.append(nums[index])     
            backtrack(index+1)            
            tmp.pop(-1)           
            
                
        backtrack(0)
        return ans