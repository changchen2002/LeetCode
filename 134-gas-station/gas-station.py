class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        tank=res=0
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0:
                res=i+1
                tank=0
        return res