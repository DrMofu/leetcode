class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:        
            if char!="]":
                stack.append(char)
                continue
            # pop
            candidate_chars = ""
            prev_char = stack.pop(-1)
            while prev_char!="[":
                candidate_chars = prev_char+candidate_chars
                prev_char = stack.pop(-1)
            # now prev_char=="["
            times=0
            order = 1
            while len(stack) and stack[-1] and ord("0")<=ord(stack[-1])<=ord("9"):
                times+=(ord(stack[-1])-ord("0"))*order
                order*=10
                stack.pop(-1)
                if len(stack)==0:
                    break
            # put char back
            for i in range(times):
                for char in candidate_chars:
                    stack.append(char)
        return "".join(stack)
                
        