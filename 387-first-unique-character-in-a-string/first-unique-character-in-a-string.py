class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap=defaultdict(int)
        for c in s:
            hashmap[c]+=1
        for i,c in enumerate(s):
            if hashmap[c]==1:
                return i
        return -1

