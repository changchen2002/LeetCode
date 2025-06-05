class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':              #s[0]not in range(1,3)是字符,不能这么比较
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=dp[1]=1
        for i in range(2,len(s)+1):
            one=int(s[i-1])
            two=int(s[i-2:i])
            if 1<=one<=9:
                dp[i]+=dp[i-1]
            if 10<=two<=26:
                dp[i]+=dp[i-2]

        return dp[-1]

