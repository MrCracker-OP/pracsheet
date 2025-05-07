graph= {
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    'C':[],
    'D':[('G',1)],
    'E':[('D',6)],
    'G':[]
}

heuristic= {
    'A':11,
    'B':6,
    'C':99,
    'D':1,
    'E':7,
    'G':0
}

def A_star(start, goal):
    queue=[(start,[],0)]
    visited=set()
    while queue:
        (node, path, cost)=queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        path=path+[node]
        if node==goal:
            return (path, cost)
        for neighbour, edge in graph.get(node,[]):
            if neighbour not in visited:
                queue.append((neighbour, path, cost+edge))
    return None


path , cost = A_star('A','G')
print("first solution: ", path, cost)
print("total cost ", cost)