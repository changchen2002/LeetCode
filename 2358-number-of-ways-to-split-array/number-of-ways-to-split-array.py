class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=cur=0
        total=sum(nums)
        for i in range(len(nums)-1):
            cur+=nums[i]
            if cur>=total-cur:
                res+=1
        return res