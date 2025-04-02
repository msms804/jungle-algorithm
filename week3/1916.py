import sys
import heapq

N = int(sys.stdin.readline()) # 정점 (도시)
M = int(sys.stdin.readline()) # 간선 (버스)

graph = [[] for _ in range(N + 1)]
# 무방향인가? -> 아니라고함
def dijkstra(graph, start, end):
    INF = float('inf')
    dist = {node: INF for node in range(N + 1)}
    # print("dist: ", dist)
    dist[start] = 0

    pq = [(start, 0)]

    while pq:
        u, here_cost = heapq.heappop(pq)

        # 게으른 삭제?
        if dist[u] < here_cost:
            continue
        for v, cost in graph[u]:
            new_cost = here_cost + cost
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (v, new_cost))

    return dist[end]

for i in range(M):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))

start_node, end_node = map(int, sys.stdin.readline().split())

# print("출발", start_node, "도착:", end_node)
# print(graph)

print("최단거리", dijkstra(graph, start_node, end_node))
