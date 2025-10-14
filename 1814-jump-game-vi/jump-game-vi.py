class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dec=deque([0])
        for i in range(1,len(nums)):
            if dec[0]<i-k:
                dec.popleft()
            nums[i]+=nums[dec[0]]
            while dec and nums[i]>=nums[dec[-1]]:
                dec.pop()
            dec.append(i)
        return nums[-1]
