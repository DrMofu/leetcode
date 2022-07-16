class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort(key=lambda x:(-len(x),x))
        for item in dictionary:
            j=0
            for char in s:
                if char==item[j]:
                    j+=1
                    if j==len(item):
                        return item
        return ""