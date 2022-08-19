# we can also use Trie
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for string in strs[1:]:
            string_len = len(string)
            common = common[:string_len]
            for i in range(min(len(common),string_len)):
                if string[i]!=common[i]:
                    common = common[:i]
                    break
        return common
        