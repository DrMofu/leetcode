class Codec:    
#     def __init__(self):
#         self.magic = "sadhuowepouqbwedoeausa"

#     def encode(self, strs):
#         """Encodes a list of strings to a single string.
        
#         :type strs: List[str]
#         :rtype: str
#         """
#         return self.magic.join(strs)
        

#     def decode(self, s):
#         """Decodes a single string to a list of strings.
        
#         :type s: str
#         :rtype: List[str]
#         """
#         return s.split(self.magic)
    
    def generate_meta(self,string):
        n = len(string)
        meta = [chr(n>>(i*8)&0xff) for i in range(4)]
        meta = meta[::-1]
        return "".join(meta)
    
    def analyze_meta(self,meta):
        n = 0
        for char in meta:
            n = n*256+ord(char)
        return n
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join(self.generate_meta(string)+string.encode('utf-8') for string in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans = []
        index = 0
        n = len(s)
        while index<n:
            meta = s[index:index+4]
            index+=4
            length = self.analyze_meta(meta)
            ans.append(s[index:index+length])
            index+=length       
        
        return ans
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))