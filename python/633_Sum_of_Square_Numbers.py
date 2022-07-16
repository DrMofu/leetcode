class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        lower = 0
        upper = int(sqrt(c)+0.5)
        while lower<=upper:
            sum_ = lower**2+upper**2
            if sum_==c:
                return True
            if sum_>c:
                upper-=1
            else:
                lower+=1
        return False