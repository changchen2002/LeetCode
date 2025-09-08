class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        used=[0]*len(nums)

        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i]=1
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=0
        backtrack([])
        return res