class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec=deque()
        res=[]
        for i,n in enumerate(nums):
            while dec and n>nums[dec[-1]]:
                dec.pop()
            dec.append(i)
            if i-k==dec[0]:
                dec.popleft()
            if i>=k-1:
                res.append(nums[dec[0]])
                
        return res       
