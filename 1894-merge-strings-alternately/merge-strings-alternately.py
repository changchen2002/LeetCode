class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p=q=0
        res=""
        while p<len(word1) and q<len(word2):
            if len(res)%2==0:
                res+=word1[p]
                p+=1
            else:
                res+=word2[q]
                q+=1
        if p<len(word1):
            res+=word1[p:]
        if q<len(word2):
            res+=word2[q:]
        return res