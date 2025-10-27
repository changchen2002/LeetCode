class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        stop2bus=defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                stop2bus[stop].add(i)
        
        q=deque()  #stop,bus,number of buses
        vis_stop=set([source])
        vis_bus=set()
        for bus in stop2bus[source]:
            q.append((bus,1))
            vis_bus.add(bus) 
        
        while q:
            bus,cnt=q.popleft()
            for stop in routes[bus]:
                if stop==target:
                    return cnt
                if stop in vis_stop:
                    continue
                vis_stop.add(stop)
                for nxt_bus in stop2bus[stop]:
                    if nxt_bus not in vis_bus:
                        vis_bus.add(nxt_bus)
                        q.append((nxt_bus,cnt+1))
        return -1
            