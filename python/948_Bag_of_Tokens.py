import collections
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        queue = collections.deque(tokens)
        max_score = 0
        score = 0
        while queue and (power>=queue[0] or score>0):
            # get score
            while queue and power>=queue[0]:
                power -= queue.popleft()
                score+=1
                max_score = max(max_score,score)
            # get power
            if queue and score>0:
                score-=1
                power+=queue.pop()
        return max_score