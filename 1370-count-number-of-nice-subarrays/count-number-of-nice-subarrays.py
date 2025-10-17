class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #i odd number-j odd number=k odd number
        hashmap=defaultdict(int)
        hashmap[0]=1
        odd=res=0
        for n in nums:
            if n%2:
                odd+=1
            res+=hashmap[odd-k]
            hashmap[odd]+=1
        return res