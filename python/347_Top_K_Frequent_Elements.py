class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        import heapq
        min_heap = []
        for key in freq:
            current_frequent = freq[key]
            if len(min_heap)<k:
                heapq.heappush(min_heap,(current_frequent,key))
            elif current_frequent>min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,(current_frequent,key))
                
        return [item[1] for item in min_heap]
                
                