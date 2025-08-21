class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def calculate(p, q):
            return (p[0]-q[0])**2 + (p[1]-q[1])**2

        points = [p1, p2, p3, p4]
        dists = []

        # 计算所有两两距离的平方
        for i in range(4):
            for j in range(i+1, 4):
                d = calculate(points[i], points[j])
                if d == 0:  # 有重合点直接返回 False
                    return False
                dists.append(d)

        # 用 set 判断是否只有两种不同长度（边长和对角线）
        if len(set(dists)) != 2:
            return False

        side = min(dists)
        diag = max(dists)

        # 统计出现次数：边长 4 次，斜边 2 次
        if dists.count(side) != 4 or dists.count(diag) != 2:
            return False

        # 对角线平方 = 2 * 边长平方
        return diag == 2 * side

