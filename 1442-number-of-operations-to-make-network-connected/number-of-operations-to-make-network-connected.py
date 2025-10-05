class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent=[i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                parent[px]=py
                return 1
            return 0

        comp=n
        for a,b in connections:
            comp-=union(a,b) #减少一个连通块
        return comp-1
            