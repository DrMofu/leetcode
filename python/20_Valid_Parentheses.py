class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses_map = {"[":"]",
                          "{":"}",
                          "(":")"}
        for char in s:
            if char in ["(","[","{"]:
                stack.append(char)
                continue
            if len(stack)==0:
                return False
            last_stack_element = stack.pop(-1)
            if parentheses_map[last_stack_element] != char:
                return
        return len(stack)==0