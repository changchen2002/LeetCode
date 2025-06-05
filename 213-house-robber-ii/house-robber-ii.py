class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def rob(nums):
            dp=[0]*(len(nums)+1)
            dp[1]=nums[0]
            for i in range(2,len(nums)+1):
                dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
            return dp[-1]

        return max(rob(nums[1:]),rob(nums[:-1]))
        