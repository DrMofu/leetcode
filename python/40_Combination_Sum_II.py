class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates_dict = {}
        for num in candidates:
            candidates_dict[num] = candidates_dict.get(num,0)+1
            
        results = []
        tmp_list = []
        
        keys = list(candidates_dict.keys())
        n = len(keys)
        print(candidates_dict,keys)
        def backtrack(index,tmp_sum):
            if tmp_sum>target:
                return
            
            if tmp_sum==target:
                # print(index,tmp_list)
                results.append(tmp_list[:])
                return            
            if index==n:
                return
            
            num = keys[index]
            for i in range(candidates_dict[num]+1):
                backtrack(index+1,tmp_sum) 
                # add this number
                tmp_list.append(num)
                tmp_sum = tmp_sum+num
                
            for i in range(candidates_dict[num]+1):
                tmp_list.pop()
            
            
        backtrack(0,0)
        return results