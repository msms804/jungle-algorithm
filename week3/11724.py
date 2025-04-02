import sys
# flood fill?
# 정점의 개수, 간선의 개수
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1) # 정점 개수만큼 visited 배열 만들기, N + 1로 해야

def dfs(v): # v는 시작할 정점
    # 1. v가 방문했다고 true로 바꾼다.
    visited[v] = True # 이걸 여기서 하면 안될듯

    # 2. v와 인접한 노드 탐색
    for n in graph[v]:
        if not visited[n]:
            dfs(n)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    
    # 1. u, v 저장하기
    graph[u].append(v) # 양방향 간선
    graph[v].append(u)



ret = 0 # 커넥티드 컴포넌트 담을 변수

# 정점의 개수 만큼 돌아야. 
for i in range(1, N + 1):
    if visited[i] == False: # 방문하지 않았다면
        dfs(i)
        ret += 1

print(ret)
