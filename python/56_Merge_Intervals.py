class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort()
        for start,end in intervals:
            if not ans:
                ans.append([start,end])
                continue
            if start>ans[-1][-1]:
                ans.append([start,end])
            else:
                ans[-1][-1] = max(ans[-1][-1],end)
        return ans