class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        def getMoney(h):
            n=len(h)
            if n==0:
                return 0
            if n==1:
                return h[0]
            dp=[0]*(n+1)
            dp[1],dp[2]=h[0],h[1]
            for i in range(2,n+1):
                dp[i]=max(dp[i-2]+h[i-1],dp[i-1])
            return dp[-1]

        return max(getMoney(nums[1:]),getMoney(nums[:-1]))