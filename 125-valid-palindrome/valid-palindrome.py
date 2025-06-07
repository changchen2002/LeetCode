class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c.lower() for c in s if c.isalnum()) #只能转换char,不能转换string
        return s==s[::-1]
        