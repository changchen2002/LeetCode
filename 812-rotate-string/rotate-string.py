class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        p1=p2=0
        for p1 in range(len(s)):
            if s[p1]==goal[0]:
                remain=len(s)-p1
                if s[p1:]==goal[:remain] and s[:p1]==goal[remain:]:
                    return True
        return False
    
    