class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        largest_num = 0
        char_set = set()
        for char in s:
            if char not in char_set:
                char_set.add(char)
                largest_num = max(largest_num,len(char_set))
            else:
                # print(char)
                left_char = s[left]
                left+=1
                while left_char!=char:
                    char_set.remove(left_char)
                    left_char = s[left]
                    left+=1
        return largest_num