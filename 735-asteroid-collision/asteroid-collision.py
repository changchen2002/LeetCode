class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            if stack and stack[-1]>0 and a<0:
                while stack and stack[-1]>0 and a<0:
                    top=stack.pop()
                    if abs(a)<top:
                        a=top
                    elif abs(a)==top:
                        a=0
            if a!=0:
                stack.append(a)
        return stack