class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for s in strs:
            zero=s.count('0')
            one=s.count('1')
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)            
        return dp[-1][-1]
        
        
        # hashmap=defaultdict()
        # for s in strs:
        #     zero,one=0,0
        #     for c in s:
        #         if c=='1':
        #             one+=1
        #         else:
        #             zero+=1
        #     hashmap[s]=(zero,one)  #相同字符串被覆盖掉了

        # dp=[[0]*(n+1) for _ in range(m+1)]

        # for key in hashmap:  #for key in hashmap 相同字符串会少一项
        #     zero,one=hashmap[key]
        #     for i in range(m,zero-1,-1):
        #         for j in range(n,one-1,-1):
        #             dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)

        # return dp[-1][-1]   
