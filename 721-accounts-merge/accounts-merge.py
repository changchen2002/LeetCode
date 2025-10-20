class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2acc={}
        parent={}
        for acc in accounts:
            for email in acc[1:]:
                parent[email]=email
                email2acc[email]=acc[0]  
        
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)]=find(y) #有问题

        for acc in accounts:
            first=acc[1]
            for email in acc[2:]:  #有问题
                union(email,first)

        emails=defaultdict(list)
        for email in parent:
            emails[find(email)].append(email) #有问题
        
        res=[]
        for root in emails:
            acc=email2acc[root]
            res.append([acc]+sorted(emails[root]))  #有问题
        
        return res


