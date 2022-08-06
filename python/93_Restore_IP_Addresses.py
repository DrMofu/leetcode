# 可继续优化
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result_list = []
        current_dot = []
        def backtrack(index):
            if len(current_dot)==3:
                # generate result
                # print(current_dot)
                first_num = s[:current_dot[0]]
                second_num = s[current_dot[0]:current_dot[1]]
                third_num = s[current_dot[1]:current_dot[2]]
                fourth_num = s[current_dot[2]:]
                if int(first_num) >255 or int(second_num)>255 or int(third_num) > 255 or int(fourth_num)>255:
                    return
                for num in [first_num,second_num,third_num,fourth_num]:
                    if len(num)>1 and num[0]=="0":
                        return
                result_string = first_num+"."+second_num+"."+third_num+"."+fourth_num
                result_list.append(result_string)
                return
            if index == len(s)-1:
                return
            current_dot.append(index+1)
            backtrack(index+1)
            current_dot.pop()
            backtrack(index+1)
            
        backtrack(0)
        return result_list