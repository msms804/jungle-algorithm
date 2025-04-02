#  2차원 0-1 BFS 코드 (Python)

from collections import deque
import sys


n = int(sys.stdin.readline())
arr = []

# 입력
for i in range(n):
    line = sys.stdin.readline().strip() # 개행 문자 제거
    arr.append(list(map(int, line))) # 각 숫자를 정수 리스트로 변환하여 추가

# 방향벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 거리배열(최소 검은 방 변경 횟수 저장)
INF = float('inf')
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0 # 시작위치



# 0-1 BFS 시작
queue = deque([(0, 0)]) # (y, x)

while queue:
    y, x = queue.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 언더플로우 오버플로우 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= n : # 여기선 0일때 제외 하면 안될듯
            continue
        
        cost = 1 if arr[ny][nx] == 0 else 0

        # 현재 계산된 경로(dist[ny][nx])보다 새로운 경로 (dist[y][x] + cost)가 더 짧다면 업데이트
        if dist[ny][nx] > dist[y][x] + cost: 
            dist[ny][nx] = dist[y][x] + cost
            if cost == 0:
                # 즉, appendleft()를 사용해서 '가중치가 작은 길'을 먼저 가도록 최적화
                queue.appendleft((ny, nx))
            else:
                queue.append((ny, nx))

print(n)
print(arr)
print(dist)
print(dist[n - 1][n - 1])