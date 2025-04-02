V = 10
adj = [[] for _ in range(V)]  # 2D 리스트로 각 정점에 대한 인접 리스트 초기화
visited = [0] * V  # 방문 여부 배열

def go(idx):
    # 출력
    print(idx)
    visited[idx] = 1

    for there in adj[idx]:
        if visited[there]:
            continue
        go(there)

# 인접 리스트 설정
adj[1].append(2)
adj[1].append(3)

adj[2].append(2)

adj[3].append(1)
adj[3].append(4)

adj[4].append(3)

# DFS 시작
for i in range(V):
    # 연결된 정점이 있고, 방문하지 않았다면
    if len(adj[i]) > 0 and visited[i] == 0:
        go(i)
