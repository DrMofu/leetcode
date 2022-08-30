import collections
class Solution(object):
    
    def __init__(self):
        self.state_good = collections.defaultdict(list)
        self.state_bad = collections.defaultdict(list)
        self.n = 0
        
    def dfs(self,good_person,states):
        states[good_person] = "G"
        for assume_bad_person in self.state_bad[good_person]:
            if not states[assume_bad_person]:
                states[assume_bad_person] = "B"
            elif states[assume_bad_person] == "G":
                return False

        for assume_good_person in self.state_good[good_person]:
            if not states[assume_good_person]:
                if not self.dfs(assume_good_person,states):
                    return False
            elif states[assume_good_person]=="B":
                return False
        return True
    
    def max_when_i_good(self,index,states):  
        if not self.dfs(index,states): # if not possible, return -n
            return -self.n    
        max_num = states.count("G")
        if None in states:
            for i in range(self.n):
                if states[i]==None:
                    new_states = states[:]
                    max_num = max(max_num,self.max_when_i_good(i,new_states))
                    states[i]="B"
        return max_num
                    
    
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        self.n = len(statements)
        
        for person,states in enumerate(statements):
            for i,num in enumerate(states):
                if num==0:
                    self.state_bad[person].append(i)
                if num==1:
                    self.state_good[person].append(i)
        
        ans = 0
        for i in range(self.n):
            states = ["B"]*i+[None]*(self.n-i)
            states[:i]
            ans = max(ans,self.max_when_i_good(i,states))
        return ans
        