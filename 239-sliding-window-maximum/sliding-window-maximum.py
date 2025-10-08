class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec=deque()
        res=[]
        for i,n in enumerate(nums):
            if dec and dec[0]<=i-k:
                dec.popleft()
            while dec and nums[dec[-1]]<n:
                dec.pop()
            dec.append(i)
            
            if i>=k-1:
                res.append(nums[dec[0]])
            
        return res


