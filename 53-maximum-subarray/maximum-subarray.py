class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=res=nums[0]
        for n in nums[1:]:
            curSum=max(n,n+curSum)
            res=max(res,curSum)
        return res