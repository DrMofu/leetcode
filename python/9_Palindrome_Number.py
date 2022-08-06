class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        num_list = []
        while x:
            num = x%10
            num_list.append(num)
            x = x//10
        left = 0
        right = len(num_list)-1
        while left<right:
            if num_list[left]!=num_list[right]:
                return False
            left+=1
            right-=1
        return True