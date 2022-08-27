import collections
class TimeMap(object):

    def __init__(self):
        self.is_sorted = {}
        self.key_info = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.key_info[key].append((timestamp,value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # binary search
        queue = self.key_info[key]
        if not queue:
            return ""
        
        left = 0
        right = len(queue)-1
        
        while left<right:
            mid = (right-left+1)//2+left # add +1, make sure the loop won't be stucked at left=mid

            if queue[mid][0]<=timestamp:
                left = mid
            else: 
                right = mid-1
            
        if queue[left][0]<=timestamp:
            return queue[left][1]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)