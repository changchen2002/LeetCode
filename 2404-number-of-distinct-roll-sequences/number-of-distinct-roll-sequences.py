class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD=10**9+7
        if n==1:
            return 6
        if n==2:
            cnt=0
            for a in range(1,7):
                for b in range(1,7):
                    if a!=b and gcd(a,b)==1:
                        cnt+=1
            return cnt
        
        dp=[[0]*7 for _ in range(7)]
        for a in range(1,7):
            for b in range(1,7):
                if a!=b and gcd(a,b)==1:
                    dp[a][b]=1
        
        for _ in range(3,n+1):
            newDP=[[0]*7 for _ in range(7)]
            for a in range(1,7):
                for b in range(1,7):
                    if dp[a][b]==0:
                        continue
                    for c in range(1,7):
                        if c!=a and c!=b and gcd(b,c)==1:
                            newDP[b][c]=(newDP[b][c]+dp[a][b])%MOD
            dp=newDP
        return sum(sum(row) for row in dp)%MOD