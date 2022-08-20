class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_list = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        ans = ""
        
        index = 0
        while num:
            if num>=map_list[index][1]:
                num-=map_list[index][1]
                ans+=map_list[index][0]
            else:
                index+=1
        return ans