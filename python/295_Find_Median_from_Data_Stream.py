import heapq
class MedianFinder(object):

    def __init__(self):
        self.large_heap = [] # min_heap
        self.small_heap = [] # max_heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small_heap)==0:
            heapq.heappush(self.small_heap,-num)
            return
        
        # put num
        top_value_of_small_heap = -self.small_heap[0]
        if num<= top_value_of_small_heap:
            heapq.heappush(self.small_heap,-num)
        else:            
            heapq.heappush(self.large_heap,num)
            
        # reshape the size of 2 heaps
        small_size = len(self.small_heap)
        large_size = len(self.large_heap)
        if small_size==large_size+2:
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)
        elif small_size+1==large_size:            
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap,-val)
        
    

    def findMedian(self):
        """
        :rtype: float
        """
        # size of min_heap >= size of max_heap        
        if len(self.small_heap)==len(self.large_heap):
            return (-self.small_heap[0]+self.large_heap[0])/2.0
        return -self.small_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()