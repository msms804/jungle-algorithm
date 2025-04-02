def topological_sort_dfs(n, edges):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    stack = []

    # 그래프 구성
    for u, v in edges:
        graph[u].append(v)

    # DFS 함수
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  # 모든 인접 노드 방문 후 push

    # 모든 노드에 대해 DFS 수행
    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]  # 스택을 뒤집어서 반환

# 예제 실행
edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
print(topological_sort_dfs(4, edges))  # [0, 1, 2, 3] (또는 다른 정렬 가능)
