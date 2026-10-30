class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        s=res=0
        for n in nums:
            s+=n
            res+=dic[s-goal]
            dic[s]+=1
        return res

