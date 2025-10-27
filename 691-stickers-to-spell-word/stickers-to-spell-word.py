class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]

#         n=len(target)
#         counts=[]
#         targetSet=set(target)
#         for s in stickers:
#             c=Counter()
#             for ch in s:
#                 if ch in targetSet:
#                     c[ch]+=1
#             counts.append(c)
# # [
# #  Counter({'w': 1, 'i': 1, 't': 1, 'h': 1}),
# #  Counter({'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}),
# #  Counter({'e': 3, 'c': 2, 'i': 1, 'n': 1, 's': 1})
# # ]
#         def dp(mask):
#             if mask==(1<<n)-1:
#                 return 0
#             res=float('inf')
#             i=0
#             while (mask>>i)&1:
#                 i+=1
#             ch=target[i]
#             for c in counts:
#                 if c[ch]==0:
#                     continue
#                 new_mask=mask
#                 remain=c.copy()
#                 for j in range(i,n):
#                     if ((mask>>j)&1)==0 and remain[target[j]]>0:
#                         remain[target[j]]-=1
#                         new_mask |=1 <<j
#                 sub=dp(new_mask)
#                 if sub!=-1:
#                     res=min(res,sub+1)
#             return res if res!=float('inf') else -1
#         return dp(0)

