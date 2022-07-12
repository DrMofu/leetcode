class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not len(points): return 0
        points.sort(key=lambda x:x[0])
        pos = points[0][1]
        counter = 1
        for ballon in points:
            if ballon[0]>pos:
                counter+=1
                pos = ballon[1]
                continue
            pos = min(pos,ballon[1])
        return counter
        