class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(idx,path):
            if idx==len(nums):
                res.append(path[:])
                return
            res.append(path[:])
            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res