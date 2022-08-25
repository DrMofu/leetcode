import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        adjacency_list = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        counter = 0
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
            degree[edge[0]]+=1            
            degree[edge[1]]+=1
        
        remove_list = []
        for node in degree:
            if degree[node]==1:
                counter+=1
                remove_list.append(node)
        
        while True:
            next_list = []
            if counter==n:
                return remove_list
            for node in remove_list:
                neighbors = adjacency_list[node]
                for neighbor in neighbors:
                    degree[neighbor]-=1
                    if degree[neighbor]==1:
                        counter+=1
                        next_list.append(neighbor)
            
            
            remove_list = next_list