class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=res=0
        types={}
        for r in range(len(fruits)):
            types[fruits[r]]=types.get(fruits[r], 0) + 1
            while len(types)>2:
                types[fruits[l]]-=1
                if types[fruits[l]]==0:
                    del types[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res