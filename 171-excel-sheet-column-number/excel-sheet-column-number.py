class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        alphaMap={chr(i+65):i+1 for i in range(26)}
        n=len(columnTitle)
        for i in range(n):
            char=columnTitle[n-1-i]
            res+=alphaMap[char]*(26**i)
        return res
