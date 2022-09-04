class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = set(range(1,10))
        for i in range(n-1):
            new_ans = set()
            for num in ans:
                last_digit = num%10
                if last_digit-k>=0:
                    new_ans.add(num*10+last_digit-k)
                if last_digit+k<=9:
                    new_ans.add(num*10+last_digit+k)
            ans = new_ans
        return list(ans)