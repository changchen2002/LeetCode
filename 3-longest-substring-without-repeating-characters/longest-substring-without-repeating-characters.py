class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=res=0
        hashset=set()
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1 #顺序别反
            hashset.add(s[r])
            res=max(res,r-l+1)
        return res
            