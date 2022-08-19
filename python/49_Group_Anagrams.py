import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def dic2str(dic):
            counter = [str(0)]*26
            for char in dic:
                counter[ord(char)-ord("a")] = str(dic[char])
            return "_".join(counter)
        
        total_hash = collections.defaultdict(list)
        for string in strs:
            str_hash = collections.defaultdict(int)
            for char in string:
                str_hash[char] += 1
                
            hashed_str = dic2str(str_hash)
            total_hash[hashed_str].append(string)
            
        ans = []
        for key in total_hash:
            ans.append(total_hash[key])            
        return ans