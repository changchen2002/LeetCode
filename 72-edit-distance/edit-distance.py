class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if m>n:
            word1,word2=word2,word1
            m,n=n,m
        dp=list(range(n+1))  #上一排

        for i in range(1,m+1):
            cur=[i]   #这一排
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    cur.append(dp[j-1])  #上一排前一个
                else:
                    cur.append(1+min(dp[j],cur[-1],dp[j-1]))  #上一排这一个,这一排上一个,上一排前一个
            dp=cur #上一排=这一排
        return dp[-1]


