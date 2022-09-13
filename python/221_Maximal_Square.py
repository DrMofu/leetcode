class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        state = [[0]*(n+1) for i in range(m+1)]
        up = [0]*(n+1)
        left = [0]*(m+1)
        ans = 0
                    
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="0":
                    up[j] = 0
                    left[i] = 0
                    matrix[i-1][j-1] = 0
                    continue
                state[i][j] = min(min(up[j],left[i]),state[i-1][j-1])+1
                ans = max(ans,state[i][j])
                up[j] = up[j]+1
                left[i] = left[i]+1
                
        return ans*ans