class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N=len(board)
        def get_pos(s):
            quot, rem = divmod(s-1, N)
            r = N - 1 - quot
            c = rem if (N - 1 - r) % 2 == 0 else N - 1 - rem
            return r, c
            
        visit=set()
        q=deque([(1,0)])
        visit.add(1)
        while q:
            s,steps=q.popleft()
            if s==N*N:
                return steps
            for nxt in range(s+1,min(s+6,N*N)+1):
                r,c=get_pos(nxt)
                if board[r][c]!=-1:
                    nxt=board[r][c]
                if nxt not in visit:
                    visit.add(nxt)
                    q.append((nxt,steps+1))
        return -1

