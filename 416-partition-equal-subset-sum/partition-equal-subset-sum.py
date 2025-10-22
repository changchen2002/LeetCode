class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=[0]*(target+1)
        dp[0]=1
        for n in nums:
            for i in range(target,n-1,-1):
                dp[i]+=dp[i-n]
            if dp[-1]>0:
                return True
        return False
        
        

        