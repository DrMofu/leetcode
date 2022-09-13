class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # intervals.append(newInterval)
        # intervals.sort()
        # ans = []
        # for item in intervals:
        #     if not ans:
        #         ans.append(item)
        #         continue
        #     if item[0]<=ans[-1][1]:
        #         ans[-1][1] = max(ans[-1][1],item[1])
        #     else:
        #         ans.append(item)
        # return ans
        
        if not intervals:
            return [newInterval]
        ans = []
        for i,item in enumerate(intervals):
            if newInterval[0]<=item[1]:
                break
            ans.append(item)            
            
        if len(ans)==len(intervals): # reach end
            ans.append(newInterval)
            return ans
        
        if newInterval[1]<intervals[i][0]: # add directly
            ans.append(newInterval)
            ans.extend(intervals[i:])
            return ans
        
        ans.append([min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])])
        
        for item in intervals[i+1:]:
            if item[0]<= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],item[1])
            else:
                ans.append(item)
        return ans