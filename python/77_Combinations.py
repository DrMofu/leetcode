class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        tmp_list = []
        
        def backtrack(current):
            if len(tmp_list)==k:
                results.append(tmp_list[:])
                return
            for i in range(current,n+1):
                tmp_list.append(i)
                backtrack(i+1)
                tmp_list.pop()
            return
        
        backtrack(1)
        return results
        