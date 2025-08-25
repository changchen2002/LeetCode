class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            res=max(res,isPalindrome(i,i),key=len)
        for i in range(1,len(s)):
            res=max(res,isPalindrome(i-1,i),key=len)
        return res