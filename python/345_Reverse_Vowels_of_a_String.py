class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a","e","i","o","u"])
        char_list = [""]*len(s)
        left = 0
        right = len(s)-1
        while left<=right:
            if s[left].lower() not in vowels:
                char_list[left] = s[left]
                left+=1
            elif s[right].lower() not in vowels:
                char_list[right] = s[right]
                right-=1
            else:
                char_list[left] = s[right]
                char_list[right] = s[left]
                left+=1; right-=1
        return "".join(char_list)