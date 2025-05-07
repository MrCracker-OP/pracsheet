graph={
    'A':['B','D','E'],
    'B':['C'],
    'C':[],
    'D':[],
    'E':['F'],
    'F':['G','H'],
    'G':[],
    'H':[],
}
def bfs(start,goal):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
            if node==goal:
                break


print("BFS :")
bfs('A','H')

def dfs(start, goal, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, goal, visited)


print("\nDFS :")
dfs('A','H')