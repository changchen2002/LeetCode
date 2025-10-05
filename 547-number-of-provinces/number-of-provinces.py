class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m,n=len(isConnected),len(isConnected[0])
        parent=[i for i in range(m)]
        size=[0]*m
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return 0
            if size[px]>size[py]:
                px,py=py,px
            parent[px]=py
            return 1
        
        connect=0
        for i in range(m):
            for j in range(n):
                if i==j:
                    continue
                if isConnected[i][j]==1:
                    connect+=union(i,j)
        return m-connect
        # 1100
        # 1101
        # 0010
        # 0101