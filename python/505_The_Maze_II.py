# 可用Dij
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if start==destination:
            return 0
        # bfs
        queue = [start+[0]]
        m = len(maze)
        n = len(maze[0])
        maze[start[0]][start[1]]=-1 # visited
        states = [[-1]*n for i in range(m)]
        
        while queue:
            row,column,distance = queue.pop(0)
            # print(row,column,distance)
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_row = row
                new_col = column
                counter = 0
                while 0<=new_row+dx<m and 0<=new_col+dy<n and maze[new_row+dx][new_col+dy]!=1:
                    new_row = new_row+dx
                    new_col = new_col+dy
                    counter+=1
                curr_distance = distance+counter
                
                if states[new_row][new_col]>curr_distance or states[new_row][new_col]==-1: # visited ignore
                    states[new_row][new_col]=curr_distance
                    queue.append([new_row,new_col,curr_distance])
                
        return states[destination[0]][destination[1]]