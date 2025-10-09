class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count=Counter(s)
        inc=[]
        seen=set()
        for c in s:
            count[c]-=1
            if c in seen:
                continue
            while inc and c<inc[-1] and count[inc[-1]]>0:
                removed=inc.pop()
                seen.remove(removed)

            inc.append(c)
            seen.add(c)
        return ''.join(inc)

