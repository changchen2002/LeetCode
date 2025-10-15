class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return max(nums[0],0)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        res=0
        for i in range(1,n-1):
            dp[i+1]=max(dp[i],dp[i-1]+nums[i])
        res=max(res,dp[n-1])
        
        dp=[0]*(n+1)
        dp[2]=nums[1]
        for i in range(2,n):
            dp[i+1]=max(dp[i],dp[i-1]+nums[i])
        res=max(res,dp[-1])
        return res