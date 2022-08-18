class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if sum(gas)<sum(cost):
            return -1
        curr_tank = 0
        start_station = 0
        for i in range(n):
            curr_tank += gas[i]-cost[i]
            if curr_tank<0:
                start_station = i+1
                curr_tank=0
        return start_station