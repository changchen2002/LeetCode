class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,total,curArray):
            if i>=len(candidates) or total>target:
                return
            if total==target:
                res.append(curArray[:])
                return 

            curArray.append(candidates[i])
            dfs(i,total+candidates[i],curArray)
            curArray.pop()

            dfs(i+1,total,curArray)
        dfs(0,0,[])
        return res
            