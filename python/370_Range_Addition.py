class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        results = [0]*length
        for start,end,val in updates:
            results[start]+=val
            if end+1<length:
                results[end+1]-=val
        for i in range(1,length):
            results[i]+=results[i-1]
        return results