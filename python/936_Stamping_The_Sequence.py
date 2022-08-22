class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        ans = []
        wildcard_queue=[]
        
        m = len(stamp)
        n = len(target)
        
        considered = [False]*n
        
        need_wildcard = []
        for start in range(n-m+1):
            not_same_pos = set()
            for pos in range(m):
                if stamp[pos]!=target[start+pos]:
                    not_same_pos.add(start+pos)
            need_wildcard.append(not_same_pos)
            
            if len(not_same_pos)==0:
                ans.append(start)
                for pos in range(m):
                    if not considered[start+pos]:
                        considered[start+pos]=True
                        wildcard_queue.append(start+pos)
                        
        while wildcard_queue:
            wildcard_pos = wildcard_queue.pop(0)
            for prev_start in range(max(0,wildcard_pos-m+1),min(n-m,wildcard_pos)+1): # pre_start's stamp contains wildcard_pos
                if wildcard_pos in need_wildcard[prev_start]:
                    need_wildcard[prev_start].remove(wildcard_pos)
                    if len(need_wildcard[prev_start])==0:
                        ans.append(prev_start)
                        for pos in range(m):
                            if not considered[prev_start+pos]:
                                considered[prev_start+pos]=True
                                wildcard_queue.append(prev_start+pos)
        if sum(considered)==n:
            return ans[::-1]
        return []