class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(n+1)
        exp = 1
        for i in range(1,n+1):
            if i==2*exp:
                exp = exp*2
            ans[i]=ans[i-exp]+1
        return ans