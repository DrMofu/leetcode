class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j],matrix[n-j-1][i],matrix[n-i-1][n-1-j],matrix[j][n-1-i] \
                    = matrix[n-j-1][i],matrix[n-i-1][n-1-j],matrix[j][n-1-i],matrix[i][j]