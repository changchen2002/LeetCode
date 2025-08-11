class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        odd=False
        length=0
        for c,freq in count.items():
            if freq%2:
                odd=True
                length+=freq-1
            else:
                length+=freq
        return length+1 if odd else length
            