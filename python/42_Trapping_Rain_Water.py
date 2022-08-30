class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        for right_index,right_h in enumerate(height):
            while len(stack) and stack[-1][1]<right_h:
                bottom_index,bottom_h = stack.pop(-1)
                if len(stack)==0: # can't hold water
                    break
                # current states: high_low_high
                left_index,left_h = stack[-1]
                distance = right_index-left_index-1
                min_height = min(left_h,right_h) - bottom_h
                ans += distance*min_height
            stack.append([right_index,right_h])
        return ans
            
            