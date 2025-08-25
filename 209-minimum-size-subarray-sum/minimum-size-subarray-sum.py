class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=cur=0
        res=len(nums)+1
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>=target:
                res=min(res,r-l+1)
                cur-=nums[l]
                l+=1
        return res if res!=len(nums)+1 else 0