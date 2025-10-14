class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        inc=deque()
        res=float('inf')
        cur=0

        for i,n in enumerate(nums):
            cur+=n 
            while inc and cur-inc[0][1]>=k:
                res=min(res,i-inc.popleft()[0])
         
            while inc and cur<=inc[-1][1]:
                inc.pop()
            inc.append((i,cur))

            if cur>=k:
                res=min(res,i+1)
            
        return res if res!=float('inf') else -1


# cur    i    n     inc
# 2      0    2      [0]
# 1      1    -1     [0,1]
# 3      2    2      [0,1,2]