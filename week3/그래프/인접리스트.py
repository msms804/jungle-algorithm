V = 4  # 4개의 정점
adj = [[] for _ in range(V)]  # 각 정점마다 연결 리스트 필요

# 그래프 간선 추가
adj[0].extend([1, 2, 3])
adj[1].extend([0, 2])
adj[2].extend([0, 1])
adj[3].extend([0])

# 첫 번째 방식: for-each 반복문
for i in range(V):
    print(f"{i} ::", end=" ")
    for there in adj[i]:  # C++의 `for (int there : adj[i])` 와 동일
        print(there, end=" ")
    print()

# 두 번째 방식: 인덱스를 사용한 접근
for i in range(V):
    print(f"{i} ::", end=" ")
    for j in range(len(adj[i])):  # C++의 `for (int j = 0; j < adj[i].size(); j++)`
        print(adj[i][j], end=" ")
    print()
