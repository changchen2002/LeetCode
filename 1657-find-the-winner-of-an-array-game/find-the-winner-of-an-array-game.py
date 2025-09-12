class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        stack=[]
        for i,a in enumerate(arr):
            if not stack:
                stack.append([a,0])
            else:
                if stack[-1][1]==k:
                    return stack[-1][0]
                if a<stack[-1][0]:
                    stack[-1][1]+=1 
                else:
                    stack.pop()
                    stack.append([a,1])
        return stack[-1][0]
            