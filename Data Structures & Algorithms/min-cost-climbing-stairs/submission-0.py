class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tcost = cost.copy()
        tcost.append(0)

        for i in range(len(tcost)-3,-1,-1):
            tcost[i] = min(tcost[i]+tcost[i+1], tcost[i]+tcost[i+2])

        print(tcost)
        return min(tcost[0],tcost[1]) 

        