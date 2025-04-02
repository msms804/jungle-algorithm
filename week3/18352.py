import sys
from collections import deque

# 도시의 개수, 도로의 개수, 거리정보, 출발 도시 번호
N, M, K, X = map(int, sys.stdin.readline().split())

visited = [0] * (N + 1) # -1로 초기화 해도 됨
graph = [[] for _ in range(N + 1)]
q = deque()

def bfs(v):
    visited[v] = 1
    q.append(v)

    while q:
        u = q.popleft()
        for n in graph[u]:
            if visited[n] == 0:
                visited[n] = visited[u] + 1
                q.append(n)

# 입력
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)

bfs(X)

result = []
for i in range(1, N + 1):
    if visited[i] == K + 1:
        result.append(i)

result.sort()

if result:
    print("\n".join(map(str, result)))
else:
    print(-1)