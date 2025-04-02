from collections import deque


N = 100

visited = [0] * N
# adj = 
nodelist = [10, 12, 14, 16, 18, 20, 22, 24]

def bfs(g, start, visited):
    queue = deque([start])
    print(queue)
    visited[start] = 1
    queue.append(g[start])

# 그래프 정의
G = {
    10: [12, 14, 16],
    12: [18, 20],
    20: [22, 24]
}

bfs(G, 10, visited)