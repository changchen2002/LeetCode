class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank)
        if endGene not in bank:
            return -1
        q=deque([(startGene,0)])
        visit={startGene}
        genes="ACGT"
        while q:
            gene,step=q.popleft()
            if gene==endGene:
                return step
            for i in range(len(gene)):
                for g in genes:
                    if gene[i]==g:
                        continue
                    new=gene[:i]+g+gene[i+1:]
                    if new in bank and new not in visit:
                        q.append([new,step+1])
                        visit.add(new)
        return -1

