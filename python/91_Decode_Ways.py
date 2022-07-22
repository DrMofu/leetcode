class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # dp = [0]*(n+1)
        # prev_char = s[0]
        # if prev_char!="0":
        #     dp[1]=1
        #     dp[0]=1
        # for index in range(2,n+1):
        #     current_char = s[index-1]
        #     one_value = int(current_char)
        #     two_value = int(prev_char+current_char)
        #     if one_value!=0:
        #         dp[index] += dp[index-1]
        #     if 10<=two_value<=26:
        #         dp[index] += dp[index-2]
        #     prev_char = current_char
        # return dp[-1]
        
        if s[0]=="0":
            return 0
        pp_val = 1
        p_val = 1
        for i,char in enumerate(s[1:]):
            pre_char = s[i]
            val_sum = 0
            if pre_char == "1" or (pre_char=="2" and char not in ["7","8","9"]):
                val_sum += pp_val
            if char != "0":
                val_sum += p_val
            pp_val,p_val = p_val,val_sum
        return p_val
