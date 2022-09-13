import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.pref_sum = []
        
        sum_ = 0
        for num in w:
            sum_+=num
            self.pref_sum.append(sum_)
            
        self.total = self.pref_sum[-1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        random_num = random.randint(0,self.total-1)
        # for i, num in enumerate(self.pref_sum):
        #     if random_num<num:
        #         return i
        left = 0
        right = len(self.pref_sum)-1
        while left<right:
            mid = (left+right)//2
            if self.pref_sum[mid]>random_num:
                right = mid
            else:
                left = mid+1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()