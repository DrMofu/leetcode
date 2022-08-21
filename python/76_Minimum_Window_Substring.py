class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        min_window = n+1
        start = end = -1
        
        t_hash = {}
        for char in t:
            t_hash[char] = t_hash.get(char,0)+1
        num_to_go = len(t)
            
        # find first target
        left = 0
        right = 0
        for right,char in enumerate(s):
            if char in t_hash:
                t_hash[char]-=1
                if t_hash[char]>=0:
                    num_to_go-=1
            if num_to_go==0:
                left_char = s[left]
                while (left_char not in t_hash) or (t_hash[left_char]<0):
                    if left_char in t_hash:
                        t_hash[left_char]+=1
                    left+=1
                    left_char = s[left]
                current_min = right+1-left
                if current_min<min_window:
                    min_window = current_min
                    start=left
                    end = right+1       
                
        
        if min_window==n+1:
            return ""
        return s[start:end]