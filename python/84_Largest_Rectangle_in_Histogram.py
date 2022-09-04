import collections
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = collections.deque([(-1,0)])        
        max_area = 0
        for right_index, right_h in enumerate(heights):
            while stack[-1][0]!=-1 and stack[-1][1]>right_h: # while not empty and not a descending stack
                middle_index, middle_h = stack.pop()
                left_index = stack[-1][0]
                width = right_index - left_index - 1
                area = width * middle_h
                max_area = max(max_area,area)
            stack.append((right_index, right_h))
                
        return max_area
            