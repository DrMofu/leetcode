class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sum_val = 0
        exp = 2**31
        while n:
            bit = n%2
            n = n//2
            sum_val += exp*bit
            exp = exp//2
        return sum_val