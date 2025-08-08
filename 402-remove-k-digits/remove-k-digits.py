class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        i=0
        for c in num:
            while stack and int(stack[-1])>int(c) and i<k:
                stack.pop()
                i+=1
            stack.append(c)

        while i<k:
            stack.pop()
            i+=1

        result = ''.join(stack).lstrip('0')

        return result if result else '0'