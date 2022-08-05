class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(start_row, start_column):
            area = 0
            queue = [[start_row,start_column]]
            while len(queue):
                area+=1
                row,column = queue.pop(0)
                for i,j in [[row-1,column],[row+1,column],[row,column-1],[row,column+1]]:
                    if i<0 or i>=m or j<0 or j>=n:
                        continue
                    if visited[i][j]:
                        continue
                    visited[i][j] = True
                    if grid[i][j]:
                        queue.append([i,j])
            return area
    
        def dfs(row,column):
            if row<0 or row>=m or column<0 or column>=n:
                return 0
            if grid[row][column]==0:
                return 0
            if visited[row][column]:
                return 0
            visited[row][column] = True
            ans = 1
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                ans+=dfs(row+dx,column+dy)
            return ans
                
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for i in range(m)]
        max_area = 0
        for row in range(m):
            for column in range(n):
                if visited[row][column]:
                    continue
                
                visited[row][column] = True
                if grid[row][column]:
                    area = bfs(row, column)
                    max_area = max(max_area,area)

                # if grid[row][column]:
                #     area = dfs(row, column)
                #     max_area = max(max_area,area)
                # visited[row][column] = True
                
                
        return max_area
                