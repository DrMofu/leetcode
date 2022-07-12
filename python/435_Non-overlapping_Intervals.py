class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not len(intervals):
            return 0
        intervals.sort(key=lambda x:x[1])
        lastest_finish_time = intervals[0][1]
        remove_intervals = 0
        for interval in intervals[1:]:
            if interval[0] < lastest_finish_time:
                remove_intervals+=1
            else:
                lastest_finish_time = interval[1]
        return remove_intervals
        
        