class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=res=0
        incq=deque()
        decq=deque()
        for r in range(len(nums)):
            while incq and incq[-1]>nums[r]:
                incq.pop()
            incq.append(nums[r])
            while decq and decq[-1]<nums[r]:
                decq.pop()
            decq.append(nums[r])

            while decq[0]-incq[0]>limit:
                if nums[l]==decq[0]:
                    decq.popleft()
                if nums[l]==incq[0]:
                    incq.popleft()
                l+=1
            res=max(res,r-l+1)
        return res
