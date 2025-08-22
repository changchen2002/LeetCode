class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=float('-inf')
        curmx=0
        for num in nums:
            curmx=max(curmx+num,num)
            res=max(curmx,res)
        return res if res!=float('-inf') else nums[0]