class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        trie = {}
        # build trie
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["word"]=word
            
        def backtrack(i,j,parent_node):
            letter = board[i][j] # no need to use visited to store flags
            current_node = parent_node[letter]
            board[i][j]="#" # used
            
            if "word" in current_node:
                ans.append(current_node["word"])
                # no need to save "word"
                current_node.pop("word")
            for row,column in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if row<0 or row>=m or column<0 or column>=n:
                    continue
                if board[row][column] in current_node:
                    backtrack(row,column,current_node)
            if len(current_node)==0:# no useful information
                parent_node.pop(letter)
            board[i][j]=letter # put it back
            
            
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i,j,trie)

        return ans