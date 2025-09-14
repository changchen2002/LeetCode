class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        res=0
        while i<len(chars):
            group=1
            while i+group<len(chars) and chars[i+group]==chars[i]:
                group+=1
            chars[res]=chars[i]
            res+=1
            if group>1:
                length=len(str(group))
                chars[res:res+length]=list(str(group))
                res+=length
            i+=group
        return res
            