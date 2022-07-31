class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        n = len(grid)
        if n==1:
            return 1
        visited = [[False]*n for i in range(n)]
        queue = []
        queue.append([0,0,1]) # row, column, level
        visited[0][0] = True
        while queue:
            row,column,level=queue.pop(0)
            for x in range(max(0,row-1),min(n,row+2)):
                for y in range(max(0,column-1),min(n,column+2)):
                    if visited[x][y] or grid[x][y]:
                        continue
                    if x==n-1 and y==n-1:
                        return level+1
                    visited[x][y] = True
                    queue.append([x,y,level+1])
        return -1