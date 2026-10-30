class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        s=res=0
        for n in nums:
            s+=n
            res+=dic[s-k]
            dic[s]+=1
        return res