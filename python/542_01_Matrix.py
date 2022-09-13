import collections
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        new_mat = [[0 if item==0 else -1 for item in line]for line in mat]
        m = len(mat)
        n = len(mat[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        queue = []
        for i,line in enumerate(new_mat):
            for j,item in enumerate(line):
                if item==0:
                    queue.append([i,j])

        next_queue_size = len(queue)
        epoch = 1
        while next_queue_size:
            for item_id in range(next_queue_size):
                x,y = queue.pop(0)
                for i in range(4):
                    if x+dx[i]>=0 and x+dx[i]<m and y+dy[i]>=0 and y+dy[i]<n and new_mat[x+dx[i]][y+dy[i]]==-1:
                        new_mat[x+dx[i]][y+dy[i]] = epoch
                        queue.append([x+dx[i],y+dy[i]])


            next_queue_size = len(queue)
            epoch+=1
        return new_mat