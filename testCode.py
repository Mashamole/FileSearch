from collections import defaultdict

graph = defaultdict(list)
graph[0].append(34)
graph[0].append(89)
graph[1].append(5)
graph[2].append(10)

visited = [False] * (max(graph)+1)

print(graph[0])
print((max(graph)+1))
