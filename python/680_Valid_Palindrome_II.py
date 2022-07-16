class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(s,left,right,num):
            if left>=right:
                return True
            if s[left]==s[right]:
                return check(s,left+1,right-1,num)
            if num==0:
                return False
            return check(s,left+1,right,num-1) or check(s,left,right-1,num-1)
        return check(s,0,len(s)-1,1)