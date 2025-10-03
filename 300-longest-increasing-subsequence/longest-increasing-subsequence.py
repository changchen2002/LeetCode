class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc=[]
        for num in nums:
            idx=bisect.bisect_left(inc,num)
            if idx==len(inc):
                inc.append(num)
            else:
                inc[idx]=num
        return len(inc)
