class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        n=len(digits)
        for i in range(n-1,-1,-1):
            if i==n-1:
                carry,digits[i]=divmod(digits[i]+1,10)
                continue
            carry,digits[i]=divmod(digits[i]+carry,10)
        if carry:
            digits.insert(0,carry)
        return digits
