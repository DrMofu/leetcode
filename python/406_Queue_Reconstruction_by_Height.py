class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        return_list = []
        people.sort(key=lambda x: (-x[0],x[1]))
        ans = []
        for person in people:
            # ans[person[1]:person[1]] = [person]
            ans.insert(person[1],person)
        return ans
        