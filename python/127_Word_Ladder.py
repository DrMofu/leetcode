import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
#         # out of time
#         if endWord not in wordList:
#             return 0

#         def distance(word1,word2):
#             counter = 0
#             for i in range(len(word1)):
#                 if word1[i]!=word2[i]:
#                     counter += 1
#             return counter==1

#         n = len(wordList)
#         adjacency = collections.defaultdict(list)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if distance(wordList[i],wordList[j]):
#                     adjacency[i].append(j)        
#                     adjacency[j].append(i)

#         queue = collections.deque()
#         visited = [False]*n
#         for i,word in enumerate(wordList):
#             if distance(beginWord,word):
#                 queue.append((i,2))
#                 visited[i]= True

#         while queue:
#             word_index, dist = queue.popleft()
#             word = wordList[word_index]
#             if word==endWord:
#                 return dist
#             for nei in adjacency[word_index]:
#                 if not visited[nei]:
#                     visited[nei]=True
#                     queue.append((nei,dist+1))             
#         return 0
        
        
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        n = len(wordList)
        adjacency = collections.defaultdict(list)    
        for word in wordList:
            for i in range(L):
                adjacency[word[:i] + "*" + word[i+1:]].append(word)
        queue = collections.deque([(beginWord,1)])
        visited = set([beginWord])
                
        while queue:
            word, dist = queue.popleft()
            for i in range(L):
                query_word = word[:i] + "*" + word[i+1:]
                for nei in adjacency[query_word]:
                    if nei in visited:
                        continue
                    if nei==endWord:
                        return dist+1
                    visited.add(nei)
                    queue.append((nei,dist+1))
        return 0
    
    
