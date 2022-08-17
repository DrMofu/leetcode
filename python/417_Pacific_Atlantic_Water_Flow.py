class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)        
        n = len(heights[0])
        
        pacific_area = set()
        pacific_queue = []
        atlantic_area = set()
        atlantic_queue = []
        
        for i in range(m):
            pacific_queue.append([i,0])
            pacific_area.add((i,0))
        for i in range(1,n):
            pacific_queue.append([0,i])
            pacific_area.add((0,i))
            
        while pacific_queue:
            row,column = pacific_queue.pop(0)
            current_height = heights[row][column]
            for next_row,next_column in [[row-1,column],[row+1,column],[row,column-1],[row,column+1]]:
                if next_row<0 or next_row>=m or next_column<0 or next_column>=n:
                    continue
                next_addr = (next_row,next_column)
                if next_addr in pacific_area:
                    continue
                next_height = heights[next_row][next_column]
                if next_height>=current_height:
                    pacific_queue.append([next_row,next_column])
                    pacific_area.add(next_addr)
                             
                    
        for i in range(m):
            atlantic_queue.append([i,n-1])
            atlantic_area.add((i,n-1))
        for i in range(n-1):
            atlantic_queue.append([m-1,i])
            atlantic_area.add((m-1,i))
            
        while atlantic_queue:
            row,column = atlantic_queue.pop(0)
            current_height = heights[row][column]
            for next_row,next_column in [[row-1,column],[row+1,column],[row,column-1],[row,column+1]]:
                if next_row<0 or next_row>=m or next_column<0 or next_column>=n:
                    continue
                next_addr = (next_row,next_column)
                if next_addr in atlantic_area:
                    continue
                next_height = heights[next_row][next_column]
                if next_height>=current_height:
                    atlantic_queue.append([next_row,next_column])
                    atlantic_area.add(next_addr)
        
        area = atlantic_area.intersection(pacific_area)
        ans = []
        for item in area:
            ans.append([item[0],item[1]])
        return ans