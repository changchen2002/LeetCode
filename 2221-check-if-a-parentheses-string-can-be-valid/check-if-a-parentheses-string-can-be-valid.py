class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False

        l=count=0
        for p,lock in zip(s,locked):
            if lock=='0':
                count+=1
            elif p=='(':
                l+=1
            elif p==')':
                if l>0:
                    l-=1
                elif count>0:
                    count-=1
                else:
                    return False
        
        balance=0 #balance 表示 “需要被匹配的左括号数”
        for i in range(len(s)-1,-1,-1):
            if locked[i]=='0':
                balance-=1
                count-=1
            elif s[i]=='(':
                balance+=1
                l-=1
            elif s[i]==')':
                balance-=1
            if balance>0:
                return False
        return l<=0

    
    # (((())(((())
    # 111111010111
    # l=2
    # count=2
    # needLeft=