class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
        for s in strs[1:]:
            i=0
            while i<len(res) and i<len(s) and res[i]==s[i]:
                i+=1
            res=res[:i]
        return res if res else ""
