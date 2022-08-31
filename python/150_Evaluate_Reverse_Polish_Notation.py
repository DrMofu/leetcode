class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char not in ["+","-","*","/"]:
                stack.append(int(char))
                continue
            second_num = stack.pop(-1)
            first_num = stack.pop(-1)
            # print(first_num,char,second_num)
            if char == "+":
                stack.append(first_num+second_num)
            elif char=="-":
                stack.append(first_num-second_num)
            elif char=="*":
                stack.append(first_num*second_num)
            elif char=="/":
                flag = 1
                if first_num*second_num<0:
                    flag=-1                
                stack.append(flag*(abs(first_num)//abs(second_num)))
        return stack[-1]
                