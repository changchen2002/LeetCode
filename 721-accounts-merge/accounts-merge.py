class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        emailToName={}

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            parent[find(x)]=find(y)
        
        for a in accounts:
            name=a[0]
            first=a[1]
            for email in a[1:]:
                if email not in parent:
                    parent[email]=email
                union(first,email)
                emailToName[email]=name

        roots=defaultdict(list)
        for email in parent:
            root=find(email)
            roots[root].append(email)
        
        res=[]
        for root,emails in roots.items():
            name=emailToName[root]
            res.append([name]+sorted(emails))
        return res