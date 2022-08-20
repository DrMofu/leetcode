class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return x
        sign = 1
        
        # convert to positive
        if x<0:
            x=-x
            sign=-1
        
        y = 0
        while x:
            y *= 10
            y += x%10
            x = x//10
        
        
        ans = sign*y
        if ans>2**31-1 or ans<-2**31:
            return 0
        return ans