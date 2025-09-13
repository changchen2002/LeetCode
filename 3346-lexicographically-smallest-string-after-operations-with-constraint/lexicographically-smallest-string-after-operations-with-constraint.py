class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res=list(s)
        for i,c in enumerate(s):
            if k==0:
                break
            toA=min(ord(c)-ord('a'),ord('z')-ord(c)+1)
            if toA<=k:
                k-=toA
                res[i]='a'
            else:
                res[i]=chr(ord(c)-k)
                k=0

        return "".join(res)

