class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            p1,p2=find(x),find(y)
            if p1==p2:
                return False
            parent[p1]=p2
            connect[0]+=1
            return True
        
        connect=[0]
        for u,v in edges:
            if not union(u,v):
                return False
        
        return connect[0]==n-1