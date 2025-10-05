class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m=len(isConnected)
        vis=set()
        def dfs(i):
            for j in range(m):
                if isConnected[i][j]==1 and j not in vis:
                    vis.add(j)
                    dfs(j)
                    
        cnc=0
        for i in range(m):
            if i not in vis:
                vis.add(i)
                cnc+=1
                dfs(i)
        return cnc