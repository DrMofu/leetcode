class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         # method 1
#         result_list = []
#         current_result = []
#         n = len(nums)
#         visited = [False]*n
        
#         def backtrack():
#             if len(current_result)==n:
#                 result_list.append(current_result[:])
#                 return
#             for i in range(n):
#                 if visited[i]:
#                     continue
#                 visited[i]=True
#                 current_result.append(nums[i])
#                 backtrack()
#                 current_result.pop()
#                 visited[i]=False            
            
#         backtrack()
#         return result_list
    
        # method 2
        
        result_list = []
        
        def backtrack(current):
            if current==n:
                result_list.append(nums[:])
                return
            for i in range(current,n):
                nums[i],nums[current] = nums[current],nums[i]
                backtrack(current+1)
                nums[i],nums[current] = nums[current],nums[i]
            
            
        n = len(nums)
        backtrack(0)
        return result_list
    
    

        