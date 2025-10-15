class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n,k=len(costs),len(costs[0])
        for i in range(1,n):
            for j in range(k):
                mnm=min(costs[i-1][color] for color in range(k) if color!=j)
                costs[i][j]+=mnm
                        
        return min(costs[-1])
        

        #[1,5,3]
        #[2+min(5,3),9+min(1,3),4+min(1,5)]
