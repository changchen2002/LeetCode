class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromic(l,r):
            while l>=0 and r< len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            res=max(res,palindromic(i,i),palindromic(i,i+1),key=len)
        return res