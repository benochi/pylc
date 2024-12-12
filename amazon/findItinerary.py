class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
            
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        itinerary = []

        def dfs(node):
            while graph[node]:
                next_dest = graph[node].popleft()
                dfs(next_dest)
            itinerary.append(node)

        dfs("JFK")
        return itinerary[::-1]