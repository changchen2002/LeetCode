class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(left,right,s):
            if left>n or right>n:
                return
            if (left+right)==n*2:
                res.append(s)
                return 
            if left<n:
                backtrack(left+1,right,s+"(")
            if right<left:
                backtrack(left,right+1,s+")")
        backtrack(0,0,"")
        return res