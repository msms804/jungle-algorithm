from collections import deque

def topological_sort(n, edges):
    # 진입차수 배열
    indegree = [0] * n

    # 그래프 인접리스트
    graph = [[] for _ in range(n)]

    # 그래프 구성 및 진입차수 계산
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1 # v가 indegree이므로 + 1 해야
    
    # 진입차수가 0인 노드들을 큐에 삽입
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []


edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
# 각각 (u, v)

print(topological_sort(4, edges))