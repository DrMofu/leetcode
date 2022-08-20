import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        ignored_fuel = [] # save "-fuel"
        
        stations.append([target,0])
        total_fuel = startFuel
        ans = 0
        for station in stations:
            # don't have enough fuel, can we get the fuel in the previous stations?
            while total_fuel<station[0]:
                if len(ignored_fuel)==0:
                    return -1
                fuel = -heapq.heappop(ignored_fuel) # get the fuel with the largest amount
                total_fuel+=fuel
                ans+=1
            # save current fuel (don't use it now)
            heapq.heappush(ignored_fuel,-station[1])
        
        return ans
    
    # or dp (time-consuming)
    # dp[i] (1 dimension array) max distance we can reach when using i gas stations
    # 为了只使用这个一维数组，需要从后向前遍历 （用二维dp数组的话遍历方向则随意了）