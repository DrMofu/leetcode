class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # [start,end)
        ans_set = set()
        n = len(s)
        # odd
        for i in range(n):
            side_len = 0
            while i-side_len>=0 and i+side_len<n and s[i-side_len]==s[i+side_len]:
                start = i-side_len
                end = i+side_len+1
                ans_set.add((start,end))
                side_len+=1
                
        # even
        for i in range(n-1):
            if s[i]!=s[i+1]:
                continue
            side_len = 0
            while i-side_len>=0 and i+1+side_len<n and s[i-side_len]==s[i+1+side_len]:
                start = i-side_len
                end = i+side_len+2
                ans_set.add((start,end))
                side_len+=1
                
        return len(ans_set)