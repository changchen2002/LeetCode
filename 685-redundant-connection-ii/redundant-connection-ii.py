class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        root=[0]*(n+1)
        cand1=cand2=None
        for u,v in edges:
            if root[v]==0:
                root[v]=u
            else:
                cand1=[root[v],v]
                cand2=[u,v]
                break

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            p1,p2=find(x),find(y)
            if p1==p2:
                return False
            parent[p1]=p2
            return True

        parent=list(range(n+1))
        for u,v in edges:
            if [u,v]==cand2:
                continue
            if not union(u,v):
                if not cand1:
                    return [u,v] #没有节点有两个父节点，只是形成了环. 删导致环的那条边
                else:
                    return cand1  #有节点有两个父节点，而且去掉第二条后仍有环. 应删第一条cand1
        return cand2 #有节点有两个父节点，但去掉第二条后图变正常. 应删第二条cand2

