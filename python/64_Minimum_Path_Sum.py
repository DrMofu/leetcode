class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
#         dp = [[0]*(n) for i in range(m)]
#         dp[0][0]=grid[0][0]
        
#         for row in range(1,m):
#             dp[row][0]=dp[row-1][0]+grid[row][0]
#         for column in range(1,n):
#             dp[0][column]=dp[0][column-1]+grid[0][column]
#         for row in range(1,m):
#             for column in range(1,n):
#                 dp[row][column] = grid[row][column] + min(dp[row-1][column],dp[row][column-1])
#         return dp[-1][-1]
            
        dp = [0]*n
        for row in range(m):
            for column in range(n):
                if column==0:
                    dp[column]=dp[column]+grid[row][column]
                elif row==0:
                    dp[column]=dp[column-1]+grid[row][column]
                else:
                    dp[column]=min(dp[column-1],dp[column])+grid[row][column]
        return dp[-1]