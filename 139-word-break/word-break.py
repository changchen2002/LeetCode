class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(len(s)+1):
            for w in wordDict:
                if i>=len(w) and s[i-len(w):i]==w and dp[i-len(w)]:
                    dp[i]=dp[i-len(w)]
        return dp[-1]