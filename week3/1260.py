import sys
from collections import deque
# 정점의 개수, 간선의 개수, 탐색 시작할 정점번호
# 4 5 1
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1) 
q = deque()

def dfs(v): # v는 시작할 정점
    # 1. v가 방문했다고 true로 바꾼다.
    visited[v] = True
    print(v, end=" ")
    # 2. v와 인접한 노드 탐색
    for n in graph[v]:
        if visited[n] == False:
            dfs(n)


def bfs(v):
    # 1. 방문처리
    visited[v] = True
    # print(v, "인접", graph[v])
    q.append(v)

    # 인접한 노드들 큐에 넣어야
    while q:
        u = q.popleft()
        print(u, end =" ")
        for n in graph[u]:
            if visited[n] == False:
                visited[n] = True
                q.append(n)
    
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프

for i in range(1, N + 1):
    graph[i].sort()


# print(graph)
dfs(V)

visited = [False] * (N + 1) # 이거 따로 초기화해야하는데
print()
bfs(V)