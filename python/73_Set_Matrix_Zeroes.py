# we can also use cell itself as indicators
# if cell[i][j] == 0 {
#     cell[i][0] = 0
#     cell[0][j] = 0
# }
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_column = set()
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for column in range(n):
                if matrix[row][column]==0:
                    zero_row.add(row)
                    zero_column.add(column)
                    
        for row in zero_row:
            matrix[row] = [0]*n
        for column in zero_column:
            for i in range(m):
                matrix[i][column] = 0