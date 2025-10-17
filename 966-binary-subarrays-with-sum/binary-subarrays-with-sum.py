class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        cur=res=0
        for n in nums:
            cur+=n
            res+=hashmap[cur-goal]
            hashmap[cur]+=1
        return res