class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hash_ = {}
        for i,num in enumerate(nums):
            if num:
                self.hash_[i]=num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        ans = 0
        for i in self.hash_:
            ans += vec.hash_.get(i,0)*self.hash_[i]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.pairs = []
#         for index, value in enumerate(nums):
#             if value != 0:
#                 self.pairs.append([index, value])

#     def dotProduct(self, vec: 'SparseVector') -> int:
#         result = 0
#         p, q = 0, 0

#         while p < len(self.pairs) and q < len(vec.pairs):
#             if self.pairs[p][0] == vec.pairs[q][0]:
#                 result += self.pairs[p][1] * vec.pairs[q][1]
#                 p += 1
#                 q += 1
#             elif self.pairs[p][0] < vec.pairs[q][0]:
#                 p += 1
#             else:
#                 q += 1

#         return result