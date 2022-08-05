class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def bfs(start_row, start_column):
            queue = [[start_row,start_column]]
            while len(queue):
                row,column = queue.pop(0)
                for i,j in [[row-1,column],[row+1,column],[row,column-1],[row,column+1]]:
                    if i<0 or i>=m or j<0 or j>=n:
                        continue
                    if visited[i][j]:
                        continue
                    visited[i][j] = True
                    if grid[i][j]=="1":
                        queue.append([i,j])
            return area
        
        def dfs(row,column):
            if row<0 or row>=m or column<0 or column>=n:
                return
            if grid[row][column]=="0":
                return
            if visited[row][column]:
                return
            visited[row][column] = True
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                dfs(row+dx,column+dy)
            return
        
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for i in range(m)]
        area = 0
        for row in range(m):
            for column in range(n):
                if visited[row][column]:
                    continue
                
                # visited[row][column] = True
                # if grid[row][column]=="1":
                #     area+=1
                #     bfs(row, column)

                if grid[row][column]=="1":
                    area+=1
                    dfs(row, column)
                visited[row][column] = True
                
                
        return area