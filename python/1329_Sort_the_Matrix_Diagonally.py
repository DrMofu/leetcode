class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        for start_row in range(m):
            queue = []
            for k in range(min(m-start_row,n)):                
                queue.append(mat[start_row+k][k])
            queue.sort()
            for k in range(min(m-start_row,n)):                
                mat[start_row+k][k] = queue[k]
                
        for start_column in range(1,n):
            queue = []
            for k in range(min(m,n-start_column)):                
                queue.append(mat[k][start_column+k])
            queue.sort()
            for k in range(min(m,n-start_column)):             
                mat[k][start_column+k] = queue[k]
                
        return mat
            