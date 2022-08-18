class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
#         # find-union
#         if len(edges)!=n-1:
#             return False
        
#         parent = list(range(n))
        
#         def find_parent(index):
#             while index!=parent[index]:
#                 index = parent[index]
#             return index
        
#         for edge in edges:
#             left_group = find_parent(edge[0])
#             right_group = find_parent(edge[1])
#             if left_group==right_group:
#                 return False
#             parent[right_group]=left_group
            
#         return True
    
    
        # DFS
        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = set()

        def dfs(node):
            if node in seen: return
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        dfs(0)
        return len(seen) == n