class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        occur = {}
        for num in arr:
            occur[num] = occur.get(num,0)+1
        sort_occur = sorted(occur.items(),key=lambda x:x[1],reverse= True)
        
        total = len(arr)
        goal = (total+1)//2
        ans = 0
        current_num = 0
        while current_num<goal:
            current_num += sort_occur[ans][1]
            ans+=1
        return ans