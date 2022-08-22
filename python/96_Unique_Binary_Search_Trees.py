class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1): # go over G[i]
            for j in range(1, i+1): # choose node j as root
                G[i] += G[j-1] * G[i-j]

        return G[n]