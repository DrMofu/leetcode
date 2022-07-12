class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if not n:
            return True
        index = 0
        for char in t:
            if char==s[index]:
                index+=1
            if index==n:
                return True
        return False
        