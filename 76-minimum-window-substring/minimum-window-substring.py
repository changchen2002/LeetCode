class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        have=l=0
        res=""
        window=defaultdict(int)
        for r in range(len(s)):
            c=s[r]
            if c in need:
                window[c]+=1
                if window[c]==need[c]:
                    have+=1
                
            while have==len(need):
                if not res or r-l+1<len(res):
                    res=s[l:r+1]
                a=s[l]
                if a in need:
                    if window[a]==need[a]:
                        have-=1
                    window[a]-=1
                l+=1
                
        return res
            
            