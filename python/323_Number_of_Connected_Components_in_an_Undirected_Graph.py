# we can also use DFS
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # make set
        parent = list(range(n))
        
        # find group
        def find_group(index):
            while index!=parent[index]:
                index=parent[index]
            return index
        
        for edge in edges:
            left_group = find_group(edge[0])
            right_group = find_group(edge[1])
            # union
            if left_group!=right_group:
                parent[right_group]=left_group
                
        counter =0
        for i,group_id in enumerate(parent):
            if i==group_id:
                counter +=1
        return counter