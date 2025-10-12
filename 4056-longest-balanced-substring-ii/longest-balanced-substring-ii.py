class Solution:
    def longestBalanced(self, s: str) -> int:
        a=b=c=0
        seen={
            ("abc", 0, 0): -1,  # 三字符等频： (a-b, a-c)
            ("ab",  0, 0): -1,  # 仅 {a,b}： (a-b, c_total)  保证 c 不变
            ("bc",  0, 0): -1,  # 仅 {b,c}： (b-c, a_total)  保证 a 不变
            ("ca",  0, 0): -1,  # 仅 {c,a}： (c-a, b_total)  保证 b 不变
            ("a",   0, 0): -1,  # 仅 a：    (b_total, c_total)  二者不变
            ("b",   0, 0): -1,  # 仅 b
            ("c",   0, 0): -1,
        }
        res=0
        for i,ch in enumerate(s):
            if ch=='a':
                a+=1
            elif ch=='b':
                b+=1
            else:
                c+=1
            keys=[
                ("abc", a - b, a - c),
                ("ab",  a - b, c),
                ("bc",  b - c, a),
                ("ca",  c - a, b),
                ("a",   b, c),
                ("b",   c, a),
                ("c",   a, b),
            ]
            for key in keys:
                if key in seen:
                    res=max(res,i-seen[key])
                else:
                    seen[key]=i
        return res
            