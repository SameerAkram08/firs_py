# graph = { 'A':['B','C','D'], 'B':['E','F'], 'C':['F'], 'D':[]}

# visited = set()

# def dfs (visited,graph,root):
#  if root not in visited:
#     print(root)
#     visited.add(root)
#     for neighbour in graph[root]:
#         dfs(visited , graph , root)

# dfs (visited,graph,'A')


graph = {'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['F'], 'D': [], 'E': [], 'F': []}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')
