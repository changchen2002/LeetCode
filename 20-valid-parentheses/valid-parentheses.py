class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c in hashmap.values():
                stack.append(c)
            if c in hashmap.keys():
                if not stack:
                    return False
                char=stack.pop()
                if char!=hashmap[c]:
                    return False
        if not stack:
            return True
        return False