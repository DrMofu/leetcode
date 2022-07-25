class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}
        for char_1 in s:
            char_dict[char_1] = char_dict.get(char_1,0)+1
        for char_2 in t:
            char_dict[char_2] = char_dict.get(char_2,0)-1
            if char_dict[char_2]<0:
                return False
        for key in char_dict:
            if char_dict[key]!=0:
                return False
        return True