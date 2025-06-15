class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(path,start,total):
            if total==target:
                res.append(path[:])
            if total>target:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                dfs(path,i,total+candidates[i])
                path.pop()
        dfs([],0,0)
        return res

