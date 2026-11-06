class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        dp1=[0]*(n+1)
        dp1[0]=dp1[1]=0
        for i in range(n-1):
            dp1[i+2]=max(dp1[i+1],dp1[i]+nums[i])
        
        dp2=[0]*(n+1)
        dp2[0]=dp2[1]=0
        for i in range(1,n):
            dp2[i+1]=max(dp2[i],dp2[i-1]+nums[i])

        return max(dp1[-1],dp2[-1])