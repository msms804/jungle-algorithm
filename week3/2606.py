import sys

# 컴퓨터 수
c = int(sys.stdin.readline())
# 컴퓨터 쌍의 수
c_pair = int(sys.stdin.readline())

visited = [False] * (c + 1)
graph = [[] for _ in range(c + 1)]


def dfs(v): # 시작 정점
    global virus_c
    visited[v] = True

    for n in graph[v]:
        if visited[n] == False: # 방문 안했더라면
            virus_c += 1
            # print("감염된 컴퓨터", n)
            dfs(n)


# 그래프에 저장하기
for _ in range(c_pair):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

virus_c = 0

dfs(1)

print(virus_c)


