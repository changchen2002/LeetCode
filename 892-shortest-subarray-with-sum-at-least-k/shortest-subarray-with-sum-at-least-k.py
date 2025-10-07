class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #前缀合越小越好, index越大越好
        #monotonic queue保证index+, 前缀和递增
        n=len(nums)
        pre=[0]
        for num in nums:
            pre.append(pre[-1]+num)
        
        q=deque()
        res=n+1
        for i in range(len(pre)):
            while q and pre[i]-pre[q[0]]>=k:
                idx=q.popleft()
                res=min(res,i-idx)
            while q and pre[i]<=pre[q[-1]]:
                q.pop()
            q.append(i)
        return res if res<=n else -1