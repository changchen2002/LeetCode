class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap={}
        res=0
        for i,num in enumerate(arr):
            hashmap[num]=hashmap.get(num-difference,0)+1
            res=max(res,hashmap[num])
        return res