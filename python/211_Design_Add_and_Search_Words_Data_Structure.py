class WordDictionary(object):
    
    def generate_node(self):
        node = {}
        node["end"]=False
        return node
        
    def __init__(self):
        self.root = self.generate_node()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = self.generate_node()
            node = node[char]
        node["end"] = True        

#     def search(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
#         candidates = [self.root]
#         new_candidates = []
        
#         for char in word:
#             for node in candidates:
#                 if char in node:
#                     new_candidates.append(node[char])
#                 elif char==".":
#                     for key in node:
#                         if key!="end":
#                             new_candidates.append(node[key])                    
#             if len(new_candidates)==0:
#                 return False
#             candidates=new_candidates
#             new_candidates = []
#         for node in candidates:
#             if node["end"]:
#                 return True
#         return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node,word):
            for i,char in enumerate(word):
                if char in node:
                    node = node[char]
                else:
                    if char==".":
                        for key in node:
                            if key!="end" and dfs(node[key],word[i+1:]):
                                return True
                    return False
            return node["end"]
        
        return dfs(self.root,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)