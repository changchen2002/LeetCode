class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        res=s=0
        for n in nums:
            s+=n
            res+=dic[s%k]
            dic[s%k]+=1

        return res