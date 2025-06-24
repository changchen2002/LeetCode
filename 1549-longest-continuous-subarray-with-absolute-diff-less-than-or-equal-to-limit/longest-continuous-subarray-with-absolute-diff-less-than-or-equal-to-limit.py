class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=res=0
        maxDeque=deque()
        minDeque=deque()
        for r in range(len(nums)):
            while maxDeque and nums[r]>maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[r])
            while minDeque and nums[r]<minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[r])
                
            while maxDeque[0]-minDeque[0]>limit:
                if nums[l]==maxDeque[0]:
                    maxDeque.popleft()
                if nums[l]==minDeque[0]:
                    minDeque.popleft()
                l+=1
            
            res=max(res,r-l+1)
        return res
