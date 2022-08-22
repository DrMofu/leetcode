class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pow_base = 4
        if n<=0:
            return False
        while n!=1:
            if n%pow_base!=0:
                return False
            n = n//pow_base
        return True