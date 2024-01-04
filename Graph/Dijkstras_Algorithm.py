import heapq

def dijkstra(graph, start):
    min_distances = {node: float('infinity') for node in graph} # infinity means haven't found a path
    min_distances[start] = 0 #start node, distance to self is 0
    pq = [(0, start)] # pq = priority queue, alwasy process node with current shortest path

    while pq:
        current_distance, current_node = heapq.heappop(pq)
       
        if current_distance > min_distances[current_node]:
            continue # skip because already found shorter path
       
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
           
            if distance < min_distances[neighbor]:
                min_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
   
    return min_distances

# Graph represented as adjacency list with weights
graph = {
    'Lansing, MI': {'Columbus, OH': 254},
    'Columbus, OH': {'Lansing, MI': 254, 'Charleston, WV': 162, 'Frankfort, KY': 186, 'Indianapolis, IN': 175},
    'Charleston, WV': {'Columbus, OH': 162, 'Frankfort, KY': 198},
    'Frankfort, KY': {'Charleston, WV': 198, 'Columbus, OH': 186, 'Indianapolis, IN': 166},
    'Indianapolis, IN': {'Columbus, OH': 175, 'Frankfort, KY': 166}
}

# Start the algorithm from 'Lansing, MI'
shortest_paths = dijkstra(graph, 'Lansing, MI')
print(shortest_paths)

