class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        #graph for storing edges
        graph = defaultdict(list)
        #deque for applying BFS
        visited = deque([[src, 0, 0]])
        #variable to hold the minimum_cost
        min_price = float('inf')
     
        for i in flights: 
            graph[i[0]].append([i[1], i[2]])

        #BFS loop
        while visited:
            city, k, price = visited.popleft()

            if price <= min_price and k <= K and city != dst:
                for neibh, price_neibh in graph[city]:
                     visited.append([neibh, k + 1, price + price_neibh])
            
            if city == dst:
                min_price = min(min_price, price)
                
        return min_price if min_price != float('inf') else -1
