class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result_list = []
        current_result = []
        n = len(nums)
        visited = [False]*n
        
        def backtrack():
            if len(current_result)==n:
                result_list.append(current_result[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not visited[i-1]: # if this number is the same as the previous number: only add this number when the previous number is added
                    continue
                visited[i]=True
                current_result.append(nums[i])
                backtrack()
                current_result.pop()
                visited[i]=False
            
            
        backtrack()
        return result_list