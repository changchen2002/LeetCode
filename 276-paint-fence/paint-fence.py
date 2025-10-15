class Solution:
    def numWays(self, n: int, k: int) -> int:
        #dp[i]=number of ways to paint fence[i]
        #dp[0]=k
        #dp[1]=k
        #dp[2]=

        # dp[0]=k red
        # dp[1]=k*k  green
        # dp[2]=(k-1)*dp[i-1]+dp[i-1] if i-1 color !=i-2 color
        if n==1:
            return k
        if n==2:
            return k*k
        dp=[0]*(n+1)
        dp[1]=k
        dp[2]=k*k
        for i in range(3,n+1):
            dp[i]=(k-1)*(dp[i-1]+dp[i-2])
        return dp[-1]
