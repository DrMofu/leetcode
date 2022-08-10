class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        tmp_list = []
        
        def backtrack(index,tmp_sum):
            if tmp_sum>target:
                return
            
            if tmp_sum==target:
                results.append(tmp_list[:])
                return            
            if index==len(candidates):
                return
            
            # don't add this number
            backtrack(index+1,tmp_sum) 
            
            # add this number
            tmp_list.append(candidates[index])
            backtrack(index,tmp_sum+candidates[index])    
            tmp_list.pop()
            
            
        backtrack(0,0)
        return results