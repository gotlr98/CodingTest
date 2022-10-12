# 문제 71
# 깊이 우선 탐색 - 빈칸을 채워 코드를 완성하시오

graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            while graph[n]:
                pass
                

    return visited

print(dfs(graph, 'E'))