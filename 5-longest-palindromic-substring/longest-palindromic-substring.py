class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=0
        res=""
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    break
                length=r-l+1
                if length>longest:
                    res=s[l:r+1]
                    longest=length
                l-=1
                r+=1


        for j in range(1,len(s)):
            l,r=j-1,j
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    break
                length=r-l+1
                if length>longest:
                    res=s[l:r+1]
                    longest=length
                l-=1
                r+=1

        return res
