import sys
from collections import deque
# 위상정렬
# 학생들 번호 1 ~ N, M은 키 비교한 횟수
N, M = map(int, sys.stdin.readline().split())
arr = []
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
arr = [i for i in range(1, N + 1)] # N배열 만들어야

# M
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

# 진입차수가 0인것들 큐에 넣는다.
q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)


while q:
    node = q.popleft()
    print(node, end=" ")

    # node와 인접한 노드들 indegree -= 1
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            # 만약 indegree가 0이라면 큐에 푸시
            q.append(neighbor)

