class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=res=0
        for r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            else:
                res=max(res,r-l+1)
        return res
        