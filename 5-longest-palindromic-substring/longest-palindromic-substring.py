class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Expand Around Center
        if len(s)<1:
            return len(s)
        
        def expand(l,r):
            while l>=0 and r< len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r] #include the previous substring

        res=s[0]
        for i in range(len(s)-1):
            odd=expand(i,i)
            even=expand(i,i+1)
            res=odd if len(odd)>len(res) else res
            res=even if len(even)>len(res) else res
        return res

        