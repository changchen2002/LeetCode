class Solution:
    def longestBalanced(self, s: str) -> int:
        res=0
        for l in range(len(s)):
            mp={}
            for r in range(l,len(s)):
                mp[s[r]]=mp.get(s[r],0)+1
                if max(mp.values())==min(mp.values()):
                    res=max(res,r-l+1)
        return res