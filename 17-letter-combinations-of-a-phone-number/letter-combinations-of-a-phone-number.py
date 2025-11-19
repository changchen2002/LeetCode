class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res=[]
        def dfs(cur,idx):
            if idx==len(digits):
                res.append(''.join(cur))
                return
            d=digits[idx]
            for letter in mapping[d]:
                cur.append(letter)
                dfs(cur,idx+1)
                cur.pop()
        
        dfs([],0)
        return res