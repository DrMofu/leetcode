class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        row_data = [[] for i in range(numRows)]
        epoch_len = 2*numRows-2
        for i,char in enumerate(s):
            index = i%epoch_len
            if index<numRows:
                row_data[index].append(char)
            else:
                index = -index+epoch_len
                row_data[index].append(char)
                
        ans = ""
        for row in row_data:
            ans += "".join(row)
        return ans