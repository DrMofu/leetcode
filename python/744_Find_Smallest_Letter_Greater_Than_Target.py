class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target>=letters[-1]:
            return letters[0]
        left = 0
        right = len(letters)-1
        # method 1
        # while left<=right:
        #     mid = left + (right-left)//2
        #     char = letters[mid]
        #     if target<char:
        #         right=mid-1
        #     else:
        #         left=mid+1
                
        # method 2
        while left<right:
            mid = left + (right-left)//2
            char = letters[mid]
            if target<char:
                right=mid
            else:
                left=mid+1
                
        return letters[left]