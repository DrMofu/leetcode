class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # counter = 0
        # for i in range(len(flowerbed)):
        #     current = flowerbed[i]
        #     if current==0:
        #         if i==0 or flowerbed[i-1]==0:
        #             if i==len(flowerbed)-1 or flowerbed[i+1]==0:
        #                 counter+=1
        #                 flowerbed[i]=1
        # return counter>=n
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i
        
        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2
        
        return count >= n
        