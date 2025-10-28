class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs=[
            ('0','0'),('1','1'),('6','9'),('8','8'),('9','6')
        ]
            
        def dfs(m,total): 
            if m==0: return [""]
            if m==1: return ['0','1','8']
            inner=dfs(m-2,total)
            res=[]
            for s in inner:
                for a,b in pairs:
                    if m==total and a=='0':
                        continue
                    res.append(a+s+b)
            return res
        
        return dfs(n,n)
        