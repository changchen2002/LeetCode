class Solution:
    def jump(self, nums: List[int]) -> int:
        res=farthest=end=0
        for i in range(len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if i==end:
                res+=1
                end=farthest
        return res