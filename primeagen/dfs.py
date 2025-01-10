class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

# Build a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Build a sample graph
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

def dfsTree(node):
    if not node:
        return
    
    print(node.value, " ")
    dfsTree(node.right)
    dfsTree(node.left)

def dfsGraph(graph, start, visit=None):
    if visit is None:
        visit = set()
    visit.add(start)
    print(start, graph.adj_list[start])
    for neighbor in graph.adj_list[start]:
        if neighbor not in visit:
            dfsGraph(graph, neighbor, visit)

# Print tests
print("DFS Traversal of Tree:")
dfsTree(root)

print("\n\nDFS Traversal of Graph:")
dfsGraph(graph, 1)