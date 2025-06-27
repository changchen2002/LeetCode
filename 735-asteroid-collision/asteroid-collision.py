class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # 处理向左移动的负数
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()  # 栈顶炸了，继续比
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # 同时炸
                break  # 当前 a 被炸掉（或同归于尽），不入栈
            else:
                # 没有碰撞 或 a 是正数 或 栈为空
                stack.append(a)
        return stack