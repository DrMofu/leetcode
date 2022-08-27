import collections
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # # Bellman_Ford O(k*m)
        # f = [float("inf")] * n
        # f[src] = 0
        # for t in range(k+1):
        #     g = f[:] #需要额外数组g, 不能在原本的f上替换。因为规则要求最多停K+1站
        #     for j, i, cost in flights:
        #         g[i] = min(g[i], f[j] + cost) 
        #     f = g
        # ans = f[dst]
        # return -1 if ans == float("inf") else ans

        
        #  Dij O(m*log(n))
        adjacency = collections.defaultdict(list)
        min_heap = []
        
        
        # build adjacency_list
        for flight in flights:
            adjacency[flight[0]].append((flight[1],flight[2]))
            
        min_heap = [(0,0, src)]
        closest = [float("inf")]*n
        stop_recode = [float("inf")]*n
        
        closest[src] = 0
        stop_recode[src] = 0
        
        while min_heap:
            distance,stop,node = heapq.heappop(min_heap)
            if node==dst:
                return distance
            
            # ignore if more than k+1 stops
            if stop==k+1:
                continue
                
            for neighbor, edge_len in adjacency[node]:
                new_neighbor_distance = distance+edge_len
                if new_neighbor_distance<closest[neighbor]:
                    closest[neighbor] = new_neighbor_distance
                    stop_recode[neighbor] = stop+1
                    heapq.heappush(min_heap,(closest[neighbor],stop+1, neighbor))
                elif stop+1 < stop_recode[neighbor]: # 尽管我目前的distance比较大，但是stop比最优的要小
                    heapq.heappush(min_heap,(new_neighbor_distance,stop+1, neighbor))
                    
        return -1