class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if total<abs(target) or (total+target)%2:
            return 0
        s=(target+total)//2
        dp=[0]*(s+1)
        dp[0]=1
        for n in nums:
            for j in range(s,n-1,-1):
                dp[j]+=dp[j-n]
        return dp[s]