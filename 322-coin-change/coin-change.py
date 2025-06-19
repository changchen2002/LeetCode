class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]+[float('inf')]*(amount)
        for i in range(amount+1):
            for coin in coins:
                if i+coin<=amount:
                    dp[i+coin]=min(dp[i]+1,dp[i+coin])
        return dp[-1] if dp[-1]!=float('inf') else -1
                    