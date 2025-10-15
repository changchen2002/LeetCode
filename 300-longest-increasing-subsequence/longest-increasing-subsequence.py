class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc=[]
        for n in nums:
            idx=bisect.bisect_left(inc,n)
            if idx==len(inc):
                inc.append(n)
            else:
                inc[idx]=n
        return len(inc)