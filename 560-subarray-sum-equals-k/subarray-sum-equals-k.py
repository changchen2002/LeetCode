class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        s=res=0
        dic[0]=1
        for n in nums:
            s+=n
            res+=dic[s-k]
            dic[s]+=1
        return res 
# n   s   res    dic
# 1   1    0       1:1
# 2   3           1:1, 3:1