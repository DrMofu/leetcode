class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(temperatures)
        stack = []
        for i,temper in enumerate(temperatures):            
            while len(stack) and stack[-1][0]<temper:
                last_temp, last_index = stack.pop(-1)
                result[last_index] = i-last_index
            stack.append([temper,i])
        return result