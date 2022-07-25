class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        str_len= len(s)
        dp = [False]*(str_len+1)
        dp[0] = True
        for pos_end in range(1,str_len+1): # str position
            for pos_start in range(pos_end):
                if not dp[pos_start]:
                    continue
                sub_str = s[pos_start:pos_end]
                if sub_str in wordSet:
                    dp[pos_end]=True
                    break
        return dp[-1]