class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        max_start = 0
        max_end = 0
        
        n = len(s)
        # odd
        for i in range(n):
            side_len = 0
            while i-side_len>=0 and i+side_len<n and s[i-side_len]==s[i+side_len]:
                side_len+=1
            side_len-=1
            string_len = 2*side_len+1
            if string_len>max_len:
                max_len=string_len
                max_start = i-side_len
                max_end = i+side_len
        
        # even
        for i in range(n-1):
            if s[i]!=s[i+1]:
                continue
            side_len = 0
            while i-side_len>=0 and i+1+side_len<n and s[i-side_len]==s[i+1+side_len]:
                side_len+=1
            side_len-=1
            string_len = 2*side_len+2
            if string_len>max_len:
                max_len=string_len
                max_start = i-side_len
                max_end = i+side_len+1
        # print(max_start,max_end+1)
        return s[max_start:max_end+1]