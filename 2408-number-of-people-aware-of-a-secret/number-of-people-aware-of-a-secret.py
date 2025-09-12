class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod=10**9+7
        dp=[0]*(n+1)
        dp[1]=1

        share=0
        for i in range(2,n+1):
            if i-delay>0:
                share+=dp[i-delay]
            if i-forget>0:
                share-=dp[i-forget]
            dp[i]=share

        res=0
        for i in range(n-forget+1,n+1):
            res+=dp[i]
        return res%mod
            