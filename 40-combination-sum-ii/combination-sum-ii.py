class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(total,idx,path):
            if total>target:
                return
            if total==target:
                res.append(path[:])
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(total+candidates[i],i+1,path)
                path.pop()
        backtrack(0,0,[])
        return res