class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s=sum(nums)
        have={n:i for i,n in enumerate(nums)}
        res=float('-inf')
        for i,n in enumerate(nums):
            target=(s-n)/2
            if target in have and have[target]!=i:
                res=max(res,n)
        return res