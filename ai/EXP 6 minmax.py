class Node:
    def __init__(self, value=None, children=None):
        self.value = value  
        self.children = children if children else [] 

def min_max(node, depth, is_maximizing_player):
  
    if not node.children:
        return node.value

    if is_maximizing_player:
        
        best_value = float('-inf')  # Start with the worst possible value for maximizing player
        for child in node.children:
            best_value = max(best_value, min_max(child, depth + 1, False))
        return best_value
    else:
        # Minimizing player's turn
        best_value = float('inf')  # Start with the best possible value for minimizing player
        for child in node.children:
            best_value = min(best_value, min_max(child, depth + 1, True))
        return best_value

# Sample Game Tree
#
#                Max
#               /   \
#            Min     Min
#           /  \    /   \
#         Max  Max Max   Max
#        /  \  /  \ / \   / \
#      3    5 6   9 1  2  0  5
#
# Min node represents a minimizing player's move, Max node represents a maximizing player's move.
# Leaf nodes are the values (3, 5, 6, etc.).

# Construct the sample tree (above)
leaf1 = Node(3)
leaf2 = Node(12)
leaf3 = Node(8)
leaf4 = Node(2)
leaf5 = Node(4)
leaf6 = Node(6)
leaf7 = Node(14)
leaf8 = Node(5)
leaf9 = Node(2)



min1 = Node(children=[leaf1, leaf2, leaf3])
min2 = Node(children=[leaf4, leaf5, leaf6])
min3=Node(children=[leaf7, leaf8, leaf9])

root = Node(children=[min1, min2,min3])

result = min_max(root, 0, True)
print(f"The optimal score for the maximizing player is: {result}")
