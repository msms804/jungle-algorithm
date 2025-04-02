import sys
from collections import deque

N, M = map(int , sys.stdin.readline().split())
miro = []
visited = [[0] * M for _ in range(N)]
q = deque()

for _ in range(N):
    miro.append(list(map(int, sys.stdin.readline().strip())))

# 출력 확인
# print(miro)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    visited[y][x] = 1
    q.append((y, x))

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = dy[i] + cur_y
            nx = dx[i] + cur_x
            
            # 언더플로우 오버플로우 체크
            if ny < 0 or ny >= N or nx < 0 or nx >= M or miro[ny][nx] == 0: continue
            if visited[ny][nx] != 0 : continue # 방문한적 있으면 x, visited == 1 이라고하면 무한루프
             
            visited[ny][nx] = visited[cur_y][cur_x] + 1
            q.append((ny, nx))

bfs(0, 0)
print(visited[N - 1][M - 1])
# print(visited)