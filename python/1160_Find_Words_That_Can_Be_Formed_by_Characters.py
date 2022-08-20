class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        limit = {}
        for char in chars:
            limit[char] = limit.get(char,0)+1
        
        num = 0
        for word in words:
            correct = True
            require = {}
            for char in word:
                if char not in limit:
                    correct = False
                    break
                    
                require[char] = require.get(char,0)+1
                if require[char]>limit[char]:
                    correct= False
                    break
                
            if correct:
                num+=len(word)
                
        return num
                    