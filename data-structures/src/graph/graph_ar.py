class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node, neighbour):
        # check if the node exists in the graph if node exists add the neighbour to the node, if not define a new node with the neighbour list 
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
            
    # https://medium.com/nerd-for-tech/graph-traversal-in-python-bfs-dfs-dijkstra-a-star-parallel-comparision-dd4132ec323a
    def bfs(self, start_node):
        visited=[]
        queue=[]    
        visited.append(start_node)
        queue.append(start_node)
        
        while queue:
            curr_node = queue.pop(0)
            for n in self.graph[curr_node]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                
        return visited
    
    
    def dfs(self, start_node):
        visited=[]
        stack=[]    
        visited.append(start_node)
        stack.append(start_node)
        
        while stack:
            curr_node = stack.pop()
            for n in self.graph[curr_node][::-1]:
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
        return visited
            


# Now, let's create a graph and add some edges.
g = Graph()
edges = [
    ('A', 'B'), 
    ('A', 'C'), 
    ('B', 'D'), 
    ('B', 'E'), 
    ('C', 'F'), 
    ('E', 'F')
]

for edge in edges:
    g.add_edge(*edge)

# Perform BFS and DFS
print("BFS:", g.bfs('A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']