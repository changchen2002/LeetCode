class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1 / val

        memo = {}

        def bfs(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            q = deque([(start, 1.0)])
            visited = {start}
            while q:
                node, prod = q.popleft()
                for nei, val in graph[node].items():
                    if nei in visited:
                        continue
                    new_prod = prod * val
                    if nei == end:
                        memo[(start, end)] = new_prod
                        memo[(end, start)] = 1 / new_prod
                        return new_prod
                    visited.add(nei)
                    q.append((nei, new_prod))
            memo[(start, end)] = -1.0
            return -1.0

        return [bfs(a, b) for a, b in queries]