class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_hash = {}
        for char in s:
            my_hash[char] = my_hash.get(char,0)+1
        for i,char in enumerate(s):
            if my_hash[char]==1:
                return i
        return -1