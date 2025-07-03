class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        res=0
        odd=False
        for freq in count.values():
            if freq%2==0:
                res+=freq
            else:
                odd=True
                res+=freq-1
        return res+1 if odd else res