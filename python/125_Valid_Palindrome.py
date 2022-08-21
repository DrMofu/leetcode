class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left<right:
            left_char = s[left].lower()
            while not (0<=ord(left_char)-ord("a")<=25 or 0<=ord(left_char)-ord("0")<=9):
                left+=1
                if left==len(s): break
                left_char = s[left].lower()
                
            right_char = s[right].lower()
            while not (0<=ord(right_char)-ord("a")<=25 or 0<=ord(right_char)-ord("0")<=9):
                right-=1
                if right==0: break
                right_char = s[right].lower()
            
            if left>=right:
                break
            
            if left_char!=right_char:
                return False
            left+=1
            right-=1
        
        return True