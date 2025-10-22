class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s=sum(stones)
        target=s//2
        dp=[0]*(target+1) 
        # abs(add-subtract)=abs(s-2*add)
        # 左边是答案,为了让左边更小,add要尽量接近s//2
        dp[0]=True
        for stone in stones:
            for i in range(target,stone-1,-1):
                dp[i]=dp[i] or dp[i-stone]
        
        for i in range(target,-1,-1):
            if dp[i]:
                return s-2*i




