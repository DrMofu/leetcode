class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        
        def backtrack(i,j,index):
            if index==len(word):
                return True
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                row = i+dx
                column=j+dy
                if row<0 or row>=m or column<0 or column>=n:
                    continue
                if used[row][column]:
                    continue
                if board[row][column]==word[index]:
                    used[row][column]=True
                    ans = backtrack(row,column,index+1)
                    used[row][column]=False
                    if ans:
                        return True
            return False
            
        m = len(board)
        n = len(board[0])
        used = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                # start backtrack
                if board[i][j] == word[0]:
                    used[i][j]=True
                    ans = backtrack(i,j,1)
                    used[i][j]=False
                    if ans:
                        return True
        return False
                    