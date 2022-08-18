class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        last_end_list = [-1]
        for item in intervals:
            assign = False
            for i in range(len(last_end_list)):                
                if item[0]>=last_end_list[i]:
                    last_end_list[i]=item[1]
                    assign=True
                    break
            if not assign:
                last_end_list.append(item[1])
        return len(last_end_list)