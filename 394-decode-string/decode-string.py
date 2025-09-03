class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        curr=""
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                stack.append((curr,num))
                curr,num="",0
            elif c==']':
                lastStr,repeat=stack.pop()
                curr=lastStr+curr*repeat
            else:
                curr+=c
        return curr

