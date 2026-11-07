class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*(n+1)
        dp[0]=0

        for i in range(m-1):
            for j in range(n):
                dp[j+1]+=dp[j]
        return dp[-1]

