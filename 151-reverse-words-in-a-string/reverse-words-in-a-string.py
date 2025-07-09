class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        i=len(s)-1
        while i>=0:
            if s[i]==" ":
                i-=1
                continue
            j=i
            while j>=0 and s[j]!=" ":
                j-=1
            res.append(s[j+1:i+1])
            i=j
        return " ".join(res)