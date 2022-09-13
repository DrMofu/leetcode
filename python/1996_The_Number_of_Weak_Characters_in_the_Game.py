# sort
import heapq
class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x:(x[0],-x[1])) # 按照attack升序排序,如果attack相同,defense 降序
        min_heap = []
        for attack, defense in properties:
            while len(min_heap) and min_heap[0]<defense:
                 heapq.heappop(min_heap)
                
            heapq.heappush(min_heap,defense)
        return len(properties) - len(min_heap)