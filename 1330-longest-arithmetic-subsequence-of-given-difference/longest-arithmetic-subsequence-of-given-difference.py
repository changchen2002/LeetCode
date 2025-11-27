class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap=defaultdict(int)
        res=0
        for i,num in enumerate(arr):
            if num-difference in hashmap:
                hashmap[num]=hashmap[num-difference]+1
            else:
                hashmap[num]=1
            res=max(res,hashmap[num])
        return res