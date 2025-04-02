V = 10
a = [[0] * V for _ in range(V)]
visited = [0] * V


def go(from_node):
    visited[from_node] = 1
    print(from_node)

    for i in range(V):
        if visited[i] == 1:
            continue
        


# 그래프 초기화
a[1][2] = 1
a[2][1] = 1
a[1][3] = 1
a[3][1] = 1
a[3][4] = 1
a[4][3] = 1

# 모든 정점에 탐색
for i in range(V):
    for j in range(V):
        if a[i][j] and visited[i] == 0:
            go(i)