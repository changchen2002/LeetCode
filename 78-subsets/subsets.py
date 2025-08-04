class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        def backtrack(path,i):
            if i==len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            backtrack(path,i+1)
            path.pop()
            backtrack(path,i+1)
        backtrack([],0)
        return res