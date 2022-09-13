class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def possible(k):
            hour = 0
            for pile in piles:
                hour+=pile//k
                if pile%k:
                    hour+=1
            return hour<=h
            
        
        left = 1
        right = max(piles)
        while left<right:
            mid = (left+right)//2
            if possible(mid):
                right = mid
            else:
                left = mid+1
        return left