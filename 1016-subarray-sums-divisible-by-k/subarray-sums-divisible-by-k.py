class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #subarray%k=0
        #(cur-prev)%k=0
        #cur%k=prev%k

        hashmap={}
        hashmap[0]=1
        cur=res=0
        for n in nums:
            cur+=n
            target=cur%k
            if target in hashmap:
                res+=hashmap[target]
            hashmap[target]=hashmap.get(target,0)+1
        return res