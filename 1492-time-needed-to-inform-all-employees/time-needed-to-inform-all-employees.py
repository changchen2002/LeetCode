class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj=defaultdict(list)
        for e,m in enumerate(manager):
            if e!=headID:
                adj[m].append(e)

        def dfs(e):
            if not adj[e]:
                return 0
            return max(dfs(sub) for sub in adj[e])+informTime[e]
        
        return dfs(headID)