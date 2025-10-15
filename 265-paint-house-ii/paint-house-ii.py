class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n,k=len(costs),len(costs[0])
        for i in range(1,n):
            min1=min2=float('inf')
            idx1=-1
            for j in range(k):
                c=costs[i-1][j]
                if c<min1:
                    min1,min2,idx1=c,min1,j
                elif c<min2:
                    min2=c
            for j in range(k):
                if j==idx1:
                    costs[i][j]+=min2
                else:
                    costs[i][j]+=min1
                        
        return min(costs[-1])
        