import collections
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        if source==target:
            return 0
        
        # each bus is a node, there is a edge between two buses if they share the same station
        n = len(routes)
        
        bus_info = []
        for route in routes:
            bus_info.append(set(route))
            
        adjacency = collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if len(bus_info[i].intersection(bus_info[j])):
                    adjacency[i].append(j)
                    adjacency[j].append(i)
        
        # start node
        queue = []
        for i,info in enumerate(bus_info):
            if source in info:
                queue.append((i,1))
                
        visited = [False]*n
        while queue:
            bus,distance = queue.pop(0)
            if target in bus_info[bus]:
                return distance
            visited[bus]=True
            for neighbor in adjacency[bus]:
                if visited[neighbor]:
                    continue
                queue.append((neighbor,distance+1))           
            
        return -1
            