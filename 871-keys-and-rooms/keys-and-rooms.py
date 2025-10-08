class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        adj=defaultdict(list)
        for i in range(n):
            adj[i]=rooms[i]

        vis=set()
        def dfs(r):
            if r in vis:
                return 
            vis.add(r)
            for nxt in adj[r]:
                dfs(nxt)
    
        dfs(0)
        return len(vis)==n