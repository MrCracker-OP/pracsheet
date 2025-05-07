graph = {
    "Frankfurt": ["Mannheim", "Wurzburg", "Kassel"],
    "Mannheim": ["Frankfurt", "Karlsruhe"],
    "Wurzburg": ["Frankfurt", "Erfurt", "Nurnberg"],
    "Kassel": ["Frankfurt", "Munchen"],
    "Karlsruhe": ["Mannheim", "Augsburg"],
    "Erfurt": ["Wurzburg"],
    "Nurnberg": ["Wurzburg", "Stuttgart", "Munchen"],
    "Stuttgart": ["Nurnberg"],
    "Augsburg": ["Karlsruhe", "Munchen"],
    "Munchen": ["Nurnberg", "Augsburg", "Kassel"]
}

def depth_limited_search(start, goal, limit, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    if limit < 0:
        return False, []
    if start == goal:
        return True, path + [start]
    
    visited.add(start)
    path.append(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            found, result_path = depth_limited_search(neighbor, goal, limit - 1, visited, path)
            if found:
                return True, result_path
    
    visited.remove(start)
    path.pop()
    return False, []

def iterative_deepening_search(start, goal):
    depth = 0
    while True:
        visited = set()
        found, path = depth_limited_search(start, goal, depth, visited)
        if found:
            return True, path
        depth += 1

depth_limited_result, depth_limited_path = depth_limited_search('Frankfurt', 'Munchen', limit=2)
print("Depth Limited Search (limit 2):", depth_limited_result, "Path:", depth_limited_path)

iterative_result, iterative_path = iterative_deepening_search('Frankfurt', 'Munchen')
print("Iterative Deepening Search :", iterative_result, "Path:", iterative_path)