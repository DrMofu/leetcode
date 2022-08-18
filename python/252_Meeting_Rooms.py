class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        last_end = -1
        for item in intervals:
            if item[0]<last_end:
                return False
            last_end = item[1]
        return True