class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique=len(set(s))
        res=0

        for unique in range(1,maxUnique+1):
            freq=[0]*26
            l=r=0
            count=0
            ok=0

            while r<len(s):
                if count<=unique:
                    idx=ord(s[r])-ord('a')
                    if freq[idx]==0:
                        count+=1
                    freq[idx]+=1
                    if freq[idx]==k:
                        ok+=1
                    r+=1
                else:
                    idx=ord(s[l])-ord('a')
                    if freq[idx]==k:
                        ok-=1
                    freq[idx]-=1
                    if freq[idx]==0:
                        count-=1
                    l+=1
                if count==unique and count==ok:
                    res=max(res,r-l)
            
        return res
                    