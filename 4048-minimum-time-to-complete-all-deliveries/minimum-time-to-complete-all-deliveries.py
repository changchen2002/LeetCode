class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        # q = deque([(0, d[0], d[1])])  # (hour, d0, d1)
        # seen = set([(0, d[0], d[1])])

        # while q:
        #     h, d0, d1 = q.popleft()
        #     if d0 == 0 and d1 == 0:
        #         return h - 1  # same adjustment as before
        #     if d0 < 0 or d1 < 0:
        #         continue

        #     if h % r[0] == 0 and h % r[1] == 0:
        #         nxt = (h + 1, d0, d1)
        #         if nxt not in seen:
        #             seen.add(nxt)
        #             q.append(nxt)
        #     elif h % r[0] == 0:
        #         for nd0, nd1 in [(d0, d1 - 1), (d0, d1)]:
        #             if nd1 >= 0:
        #                 nxt = (h + 1, nd0, nd1)
        #                 if nxt not in seen:
        #                     seen.add(nxt)
        #                     q.append(nxt)
        #     elif h % r[1] == 0:
        #         for nd0, nd1 in [(d0 - 1, d1), (d0, d1)]:
        #             if nd0 >= 0:
        #                 nxt = (h + 1, nd0, nd1)
        #                 if nxt not in seen:
        #                     seen.add(nxt)
        #                     q.append(nxt)
        #     else:
        #         for nd0, nd1 in [(d0 - 1, d1), (d0, d1 - 1)]:
        #             if nd0 >= 0 and nd1 >= 0:
        #                 nxt = (h + 1, nd0, nd1)
        #                 if nxt not in seen:
        #                     seen.add(nxt)
        #                     q.append(nxt)
        def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a

        a=d[0]+(d[0]-1)//(r[0]-1)
        b=d[1]+(d[1]-1)//(r[1]-1)
        dtot=d[0]+d[1]
        rgcd=r[0]*r[1]//gcd(r[0],r[1])
        c=dtot+(dtot-1)//(rgcd-1)
        return max(a,b,c)


        