# 可继续优化节约空间，懒得写了
# 其他方法：快速幂
class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]*n
        e = [1]*n
        i = [1]*n
        o = [1]*n
        u = [1]*n
        for j in range(1,n):
            a[j] = (e[j-1]+i[j-1]+u[j-1])%int(1e9+7)
            e[j] = (a[j-1]+i[j-1])%int(1e9+7)
            i[j] = (e[j-1]+o[j-1])%int(1e9+7)
            o[j] = (i[j-1])%int(1e9+7)
            u[j] = (i[j-1]+o[j-1])%int(1e9+7)
        
        
        return (a[-1]+e[-1]+i[-1]+o[-1]+u[-1])%int(1e9+7)


        # # 快速幂方法：来自leetcode.cn官方答案
        # import numpy as np
        # factor = np.mat([(0, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 1, 0, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0)], np.dtype('O'))
        # res = np.mat([(1, 1, 1, 1, 1)], np.dtype('O'))
        # n -= 1
        # while n > 0:
        #     if n % 2 == 1:
        #         res = res * factor % 1000000007
        #     factor = factor * factor % 1000000007
        #     n = n // 2
        # return res.sum() % 1000000007