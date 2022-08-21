import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        
        # generate rules
        rules = set()
        for i in range(n-1):
            first_word = words[i]
            second_word = words[i+1]
            for j in range(len(first_word)):
                if j>= len(second_word):
                    return "" # not valid
                if first_word[j]==second_word[j]:
                    continue
                rules.add((first_word[j],second_word[j]))
                break
                
        # generate graph
        adjacency = collections.defaultdict(list)        
        char_set = set()
        for word in words:
            for char in word:
                char_set.add(char)
        in_degree = {}
        for char in char_set:
            in_degree[char] = 0
            
        for rule in rules:
            adjacency[rule[0]].append(rule[1])            
            in_degree[rule[1]] = in_degree[rule[1]]+1
        
        
        # BFS
        node_num = len(char_set)
        queue = []
        ans = ""
        for key in in_degree:
            if in_degree[key]==0:
                queue.append(key)
                
        while queue: # we can modify this part to calculate how many possible results
            node = queue.pop(0)
            ans += node
            for neighbor in adjacency[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
                    
        if len(ans)!=node_num: # no valid results
            return ""
        
        return ans
        