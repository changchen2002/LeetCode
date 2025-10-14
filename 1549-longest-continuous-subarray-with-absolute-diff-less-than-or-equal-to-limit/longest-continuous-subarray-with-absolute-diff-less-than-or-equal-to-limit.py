class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec=deque()
        inc=deque()
        l=res=0
        for i,n in enumerate(nums):
            while dec and n>nums[dec[-1]]:
                dec.pop()
            dec.append(i)
            while inc and n<nums[inc[-1]]:
                inc.pop()
            inc.append(i)
            while nums[dec[0]]-nums[inc[0]]>limit:
                if l==dec[0]:
                    dec.popleft()
                if l==inc[0]:
                    inc.popleft()
                l+=1
            res=max(res,i-l+1)
            
        return res


        