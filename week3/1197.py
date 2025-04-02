# 최소신장(스패닝)트리 : 가중치의 합이 최소인 트리
import sys
sys.setrecursionlimit(10**6)  # (비추천) 재귀 제한을 늘릴 수 있지만 근본 해결책은 아님

V, E = map(int, sys.stdin.readline().split())

edges = []
ret = 0
parent = [i for i in range(V + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) # 이 부분 헷갈림..
    return parent[x]


def union_parent(a , b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent (a, b):
    return get_parent(a) == get_parent(b)
    
for i in range(E):
    # A번 정점, B번 정점, 가중치 C
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()

for cost, a, b in edges:
    # 부모가 다르다면 union
    if not same_parent(a, b):
        union_parent(a, b)
        ret += cost

print("가중치", ret)
# 출력 확인
# print("정렬된 간선 리스트:", edges)


