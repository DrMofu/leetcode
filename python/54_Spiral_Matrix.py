class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        speed = [[0,1],[1,0],[0,-1],[-1,0]]
        speed_index = 0
        
        row = column = 0
        for  i in range(m*n):
            ans.append(matrix[row][column])
            matrix[row][column]= "V"
            next_row = row+speed[speed_index][0]
            next_column = column+speed[speed_index][1]
            if next_row<0 or next_row>=m or next_column<0 or next_column>=n or matrix[next_row][next_column]=="V":
                speed_index = (speed_index+1)%4
                next_row = row+speed[speed_index][0]
                next_column = column+speed[speed_index][1]
            row,column = next_row,next_column
        return ans