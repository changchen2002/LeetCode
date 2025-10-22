class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(1,n+1):
            for w in wordDict:
                length=len(w)
                if i>=0 and s[i-length:i]==w:
                    dp[i]=dp[i] or dp[i-length]
        
        return dp[-1]
                