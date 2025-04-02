import sys
from collections import deque

# 근데 dfs로는 어케품?
N = int(sys.stdin.readline())
# 부모 정보를 저장할 리스트
parent = [0] * (N + 1)
visited = [False] * (N + 1)
q = deque()

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    visited[node] = True
    q.append(node)

    while q:
        u = q.popleft()

        for v in graph[u]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
                parent[v] = u # 부모노드 u를 parents 배열에 저장

bfs(1)

# print(parent)

for i in range(2, N + 1):
    print(parent[i])
