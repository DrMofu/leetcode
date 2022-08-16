class Trie(object):
    
    def generate_node(self):
        node = {}
        node["end"]=False
        return node
        
    def __init__(self):
        self.root = self.generate_node()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = self.generate_node()
            current_node = current_node[char]
        current_node["end"]=True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return current_node["end"]
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)