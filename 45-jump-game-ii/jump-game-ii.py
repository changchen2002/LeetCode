class Solution:
    def jump(self, nums: List[int]) -> int:
        res=jump=farthest=0
        for i in range(len(nums)):
            if i>jump:
                res+=1
                jump=farthest
            farthest=max(farthest,i+nums[i])
        return res
            
