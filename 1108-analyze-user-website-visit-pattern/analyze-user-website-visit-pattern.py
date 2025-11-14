class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users=defaultdict(list)
        for u,t,w in sorted(zip(username,timestamp,website)):
            users[u].append(w)
        
        patterns=Counter()
        for user,sites in users.items():
            patterns.update(Counter(set(combinations(sites,3))))
        
        return max(sorted(patterns),key=patterns.get)