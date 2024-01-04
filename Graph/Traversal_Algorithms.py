
graph = {
    'Michigan': ['Indiana', 'Ohio'],
    'Ohio': ['Michigan', 'Indiana', 'Kentucky', 'West Virginia'],
    'Indiana': ['Michigan', 'Ohio', 'Kentucky'],
    'Kentucky': ['Indiana', 'Ohio', 'West Virginia'],
    'West Virginia': ['Ohio', 'Kentucky']
}

def dfs(visited, graph, node):
    if node not in visited:
        print(f'Visited {node}')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Let's start with an empty set to track the visited nodes
visited = set()

# We can start our traversal at any node, let's start at 'Ohio'
print("Depth-First")
dfs(visited, graph, 'Ohio')


from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f'Visited {node}')
            visited.add(node)
            # Convert graph[node] to a set for the set difference, then back to a list to extend the queue.
            queue.extend(list(set(graph[node]) - visited))

# Starting BFS traversal from 'Ohio'
print("Breadth-First")
bfs(graph, 'Ohio')