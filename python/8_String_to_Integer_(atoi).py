class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        
        first = True
        num = 0
        flag = 1
        for i,char in enumerate(s):
            if first:
                if char==" ":
                    continue
                elif char=="-":
                    flag = -1
                elif char=="+":
                    pass
                elif char.isdigit():
                    num = int(char)
                else:
                    return 0
                first = False
            else:
                if char.isdigit():
                    num = num*10+int(char)
                else:
                    break
                    
        num = flag*num
        
        if num>INT_MAX:
            return INT_MAX
        elif num<INT_MIN:
            return INT_MIN
        
        return num