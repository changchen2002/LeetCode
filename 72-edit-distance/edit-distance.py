class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if m>n:
            word1,word2=word2,word1
            m,n=n,m
        dp=list(range(n+1))

        for i in range(1,m+1):
            cur=[i]
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    cur.append(dp[j-1])
                else:
                    cur.append(1+min(dp[j],cur[-1],dp[j-1]))
            dp=cur
        return dp[-1]


