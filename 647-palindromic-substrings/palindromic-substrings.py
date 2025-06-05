class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        def palindrome(l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        for i in range(len(s)):
            res+=palindrome(i,i)
        for i in range(1,len(s)):
            res+=palindrome(i-1,i)
        return res
