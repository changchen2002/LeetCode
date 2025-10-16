class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for c in coins:  #这个顺序是求有多少种组合
            for a in range(c,amount+1): #a和c顺序反过来则是求有多少种不同顺序
                dp[a]+=dp[a-c]
        return dp[amount]
