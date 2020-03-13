import bisect
class Solution:
    def findItinerary(self, tickets: list) -> list:
        ans = []
        itineraries = {}
        
        for src, dest in tickets:
            if src not in itineraries:
                itineraries[src] = []
                
            bisect.insort_left(itineraries[src], dest)
        
        for src, dest in itineraries.items():
            itineraries[src] = dest[::-1]
            
        def dfs(src):            
            while src in itineraries and itineraries[src]:
                dfs(itineraries[src].pop())
                
            ans.append(src)
        
        dfs("JFK")
        return ans[::-1]