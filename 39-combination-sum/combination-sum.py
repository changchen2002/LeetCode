class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(i,path,curr):
            if curr==target:
                res.append(path[:])  #列表是可变对象,后续会变,要拷贝放进res
                return
            if i==len(candidates) or curr>target:
                return
            path.append(candidates[i])
            backtrack(i,path,curr+candidates[i])
            path.pop()
            backtrack(i+1,path,curr)
        backtrack(0,[],0)
        return res