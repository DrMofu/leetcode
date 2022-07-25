class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char,0)+1
        output = 0
        for char in char_dict:
            output+=char_dict[char]//2*2            
        if output<len(s): # at least one odd
            output+=1
        return output