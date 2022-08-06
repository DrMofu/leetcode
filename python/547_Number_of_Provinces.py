class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False]*n
        province_num = 0
        
        def dfs(i):
            state = isConnected[i]
            for j,connect in enumerate(state):
                if connect and not visited[j]:
                    visited[j] = True
                    dfs(j)
                    
        
        for i in range(n):
            if visited[i]:
                continue
            province_num += 1
            visited[i] = True
            dfs(i)
        return province_num