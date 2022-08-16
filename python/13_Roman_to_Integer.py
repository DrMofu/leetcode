class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # greedy
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
              "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        total_num = 0
        n = len(s)
        i = 0
        while i<n:
            if i+2<=n and s[i:i+2] in dic:
                total_num += dic[s[i:i+2]]
                i+=2
            else:
                total_num += dic[s[i]]
                i+=1
        return total_num