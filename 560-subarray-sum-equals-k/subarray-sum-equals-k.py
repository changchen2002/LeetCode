class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        cur=res=0
        for i in range(len(nums)):
            cur+=nums[i]
            res+=prefix[cur-k] 
            prefix[cur]+=1 
        return res