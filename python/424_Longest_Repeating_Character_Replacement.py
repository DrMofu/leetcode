class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # brute O(N^2)
        # 假设left是重复字符串开始的起点。for i in range(n), 找最远右端点
        
        
        
        # 双指针
        counter = [0]*26
        left = 0
        for right,char in enumerate(s):
            counter[ord(char)-ord("A")] +=1
            string_len = right-left+1
            # 如果满足条件 (相同字符数+可修正的数目>=整个字符串长度)，则记录最大值 (这里不需要额外变量来，因为right-left+1是最大值)
            if max(counter)+k>=string_len:
                pass
            else:
                counter[ord(s[left])-ord("A")]-=1
                left+=1
        return right-left+1