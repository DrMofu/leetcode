class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(numbers)-1
        while head!=tail:
            total_sum = numbers[head]+numbers[tail]
            if total_sum == target:
                return [head+1,tail+1]
            if total_sum > target:
                tail-=1
            else:
                head+=1
        return []