class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_index = 0
        for cookie_size in s:
            if cookie_size>=g[child_index]:
                child_index+=1
            if child_index==len(g):
                break
        return child_index