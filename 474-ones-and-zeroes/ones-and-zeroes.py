class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        hashmap=defaultdict()
        for s in strs:
            zero,one=0,0
            for c in s:
                if c=='1':
                    one+=1
                else:
                    zero+=1
            hashmap[s]=(zero,one)

        dp=[[0]*(n+1) for _ in range(m+1)]

        for s in strs:  #for key in hashmap 不要这样.key是什么不清晰
            zero,one=hashmap[s]
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)

        return dp[-1][-1]   
