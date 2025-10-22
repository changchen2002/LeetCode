class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2: #别忘
            return max(nums)

        dp=[0]*(n+1)
        dp[1],dp[2]=nums[0],nums[1]

        for i in range(2,n+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        
        return dp[-1]

# [1,2,3,1] 
# n=4
# dp=[0,1,2,4,4]
# i     dp[i]
# 3      dp[3]=max(dp[1]+3,dp[2])=4
# 4      dp[4]=max(dp[2]+1,dp[3])=4
# 4

[2,1]