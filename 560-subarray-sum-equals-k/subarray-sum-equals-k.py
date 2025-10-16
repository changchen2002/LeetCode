class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        cur=res=0
        for n in nums:
            cur+=n
            res+=hashmap[cur-k]
            hashmap[cur]+=1
        return res