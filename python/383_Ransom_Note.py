import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        have = collections.defaultdict(int)
        for char in magazine:
            have[char] += 1
            
        for char in ransomNote:
            have[char] -= 1
            if have[char]<0:
                return False
        
        return True
            