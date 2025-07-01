class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=dp[1]=1
        for i in range(2,len(s)+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1]  #一位能解码
            two=int(s[i-2:i])
            if 10<=two<=26: #两位能解码
                dp[i]+=dp[i-2]
            
        return dp[-1]
            
