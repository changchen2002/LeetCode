class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        size=[0]*(n+1)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            if size[px]>size[py]:
                px,py=py,px
            parent[px]=py
            size[py]+=size[px]
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]