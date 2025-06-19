from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need=Counter(t)
        window={}
        have,needCount=0,len(need)
        res=""
        l=0

        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have+=1
            
            while have==needCount:
                if not res or (r-l+1)<len(res):
                    res=s[l:r+1]
                
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        
        return res
        