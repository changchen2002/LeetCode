class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        bad=set(forbidden)
        l=res=0
        for r in range(len(word)):
            for L in range(1,11):
                if r-L+1<l:
                    break
                if word[r-L+1:r+1] in bad:
                    l=r-L+2
                    break
            res=max(res,r-l+1)
        return res
                