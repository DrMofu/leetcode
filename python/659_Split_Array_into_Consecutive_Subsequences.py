# hash + greedy
import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_hash = collections.defaultdict(int)
        for num in nums:
            num_hash[num] += 1
            
        end_with = collections.defaultdict(int)
        
        # greedy
        
        for num in sorted(num_hash.keys()):
            while num_hash[num]:
                if end_with[num-1]>0:
                    num_hash[num]-=1
                    end_with[num-1]-=1
                    end_with[num]+=1
                elif num_hash[num+1]>0 and num_hash[num+2]:
                    num_hash[num]-=1
                    num_hash[num+1]-=1
                    num_hash[num+2]-=1
                    end_with[num+2]+=1
                else:
                    return False
        return True
        