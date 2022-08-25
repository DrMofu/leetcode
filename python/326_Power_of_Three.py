class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        base = 3
        while n%base==0:
            n = n//base
            
        return n==1