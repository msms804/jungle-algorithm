N = 6
visited = [0] * N
adj = [[] for _ in range(N)] 

def dfs(u):
    visited[u] = 1
    print(u)
    for v in adj[u]:
        if visited[v] == 0:
            dfs(v)
    print(u, "로부터 시작된 함수가 종료되었습니다.")
    return

adj[1].append(2)
adj[1].append(3)
adj[2].append(4) # 양방향?
adj[4].append(2)
adj[2].append(5)

dfs(1)

