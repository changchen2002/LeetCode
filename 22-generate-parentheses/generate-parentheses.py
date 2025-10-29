class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(l,r,path):
            if l==n and r==n:
                res.append(''.join(path))
            if l<n:
                backtrack(l+1,r,path+["("])
            if l>r:
                backtrack(l,r+1,path+[')'])
        backtrack(0,0,[])
        return res
                