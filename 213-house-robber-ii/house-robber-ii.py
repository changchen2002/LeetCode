class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def rob(arr):
            dp=[0]*(len(arr)+1)
            dp[1]=arr[0]
            for i in range(2,len(arr)+1):
                dp[i]=max(dp[i-1],arr[i-1]+dp[i-2])
            return dp[-1]

        return max(rob(nums[1:]),rob(nums[:-1]))
        