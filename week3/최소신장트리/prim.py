import sys
import heapq
from collections import defaultdict



def prim(start, n, edges):
    graph = defaultdict(list)
    for v, w, cost in edges:
        graph[v].append((cost, w))
        graph[w].append((cost, v))

    # print(graph)

    visit = [False] * (n + 1)
    pq = [(0, start)] # (가중치, 정점)
    total = 0

    while pq:
        cost, v = heapq.heappop(pq) # 가장 작은 비용의 간선 선택
        if visit[v]:
            continue

        visit[v] = True
        total += cost # 최소 신장 트리 비용 추가

        for next_cost, next_v in graph[v]: # v에 연결된 모든 간선 확인
            if not visit[next_v]:  # 아직 방문하지 않았다면 최소힙에 추가 
                heapq.heappush(pq, (next_cost, next_v))

    print(total)

if __name__ == "__main__":
    n = int(sys.stdin.readline()) # 정점 개수
    m = int(sys.stdin.readline()) # 간선 개수
    # edges 리스트에 (정점1, 정점2, 가중치) 형태의 튜플로 저장
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)] # 간선 리스트
    prim(1, n, edges) # 시작노드 : 1