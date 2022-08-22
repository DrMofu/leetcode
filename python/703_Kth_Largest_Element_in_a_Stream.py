import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)
            
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap,val)
        elif val>self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap,val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)