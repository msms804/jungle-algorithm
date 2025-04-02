import heapq

def dijkstra(graph, start):
    INF = float('inf')
    dist = {node: INF for node in graph}
    # print("거리", dist)
    dist[start] = 0
    pq = [(0, start)] # (거리, 정점)

    while pq:
        here_cost, u = heapq.heappop(pq)

        # 느긋한 삭제(낡은 값 무시)
        # 정점이 같은게 큐에 들어갔을때 코스트 높은것 무시
        if dist[u] < here_cost:
            continue

        for v, weight in graph[u]:
            new_cost = here_cost + weight
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
        # print(dist)
        
    return dist



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)