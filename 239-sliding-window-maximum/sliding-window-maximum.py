class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec=deque()
        l=0
        res=[]
        for r in range(len(nums)):
            while dec and nums[r]>nums[dec[-1]]:
                dec.pop()
            dec.append(r)
            if dec[0]<=r-k:
                dec.popleft()
            if r>=k-1:
                res.append(nums[dec[0]])
        return res

# l   r    dec            res
# 0   0    1   
# 0   1    3
# 0   2    3 -1          3
# 1   3    3 -1 -3       3,3
# 2   4    5      