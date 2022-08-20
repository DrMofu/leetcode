class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(point1,point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        # import heapq
#         min_heap = []
#         n = len(points)
#         for i in range(n):
#             for j in range(i):
#                 dis = distance(points[i],points[j])
#                 heapq.heappush(min_heap,(dis,(i,j)))
#         print(min_heap)
        
#         # make set
#         parent = list(range(n))        
#         def find_group(index):
#             while index!=parent[index]:
#                 index = parent[index]
#             return index
        
#         # union
#         cost = 0
#         group_num = n
#         while min_heap and group_num!=1:
#             dis,(i,j) = heapq.heappop(min_heap)
#             first_group = find_group(i)
#             second_group = find_group(j)
#             if first_group!=second_group:
#                 parent[second_group] = first_group
#                 parent[j] = first_group
#                 group_num-=1
#                 cost+=dis
#         return cost

        # prim algorithm
        n = len(points)
        in_mst = [False]*n
        mst_dis = [float("inf")]*n
        mst_dis[0]=0
        
        mst_cost = 0
        node_used = 0
        while node_used<n:
            # find next node
            min_dist = float("inf")
            node = -1
            for i in range(n):
                if in_mst[i]:
                    continue
                if mst_dis[i]<min_dist:
                    min_dist = mst_dis[i]
                    node = i
            # use this node:
            node_used+=1
            in_mst[node]=True
            mst_cost+=min_dist
            # update mst_dis
            for j in range(n):
                if in_mst[j]:
                    continue
                dis = distance(points[node],points[j])
                if dis<mst_dis[j]:
                    mst_dis[j]=dis
        
        return mst_cost