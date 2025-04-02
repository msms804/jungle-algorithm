import sys
from collections import deque
# 0-1 bfs (가중치가 0 또는 1)

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    line = sys.stdin.readline().strip() # 개행 문자 제거
    arr.append(list(map(int, line))) # 각 숫자를 정수 리스트로 변환하여 추가


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque([(0, 0)])

# 최단거리 구해야 할때는 무한으로 초기화 해놓고 시작
INF = float('inf')
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0

while q:
    cur_y, cur_x = q.popleft()

    for i in range(4):
        ny = dy[i] + cur_y
        nx = dx[i] + cur_x

        # 오버플로, 언더플로 체크
        if(ny < 0 or ny >= n or nx < 0 or nx >= n):
            continue
        
        cost = 1 if arr[ny][nx] == 0 else 0

        if dist[ny][nx] > dist[cur_y][cur_x] + cost:
            dist[ny][nx] = dist[cur_y][cur_x] + cost
            if cost == 1:
                q.append((ny, nx))
            else:
                q.appendleft((ny, nx))

print(dist[n - 1][n - 1])