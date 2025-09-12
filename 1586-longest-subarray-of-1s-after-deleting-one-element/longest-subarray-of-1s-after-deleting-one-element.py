class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res=l=zero=0
        hasZero=0
        for r in range(len(nums)):
            if nums[r]==0:
                hasZero=1
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1
            res=max(res,r-l-zero+1)
        return res if hasZero else res-1