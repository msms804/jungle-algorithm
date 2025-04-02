# 이진검색트리를 전위순회한 결과가 주어졌을때 
# 후위순회한 결과를 구하는 프로그램

# 이진검색트리에서 중위 순회하면 소팅한 결과가 나옴

import sys
sys.setrecursionlimit(10**9)

pre = []

while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def post_order (root_idx, last_idx):
    # 재귀 중단 조건
    if root_idx > last_idx:
        return
    
    # 루트 노드
    root = pre[root_idx]

    # 오른쪽 서브트리의 시작 인덱스를 담을 변수
    right_start_idx = root_idx + 1

    while right_start_idx <= last_idx and pre[right_start_idx] < root:
        # if pre[right_start_idx] > root:
            # break
        right_start_idx += 1

    # 왼쪽 서브 트리 : 루트의 다음 ~ 루트보다 크지 않은 노드
    post_order(root_idx + 1, right_start_idx - 1)

    # 오른쪽 서브 트리: 루트보다 큰 노드 ~ 끝
    post_order(right_start_idx, last_idx)

    # 부모노드 출력
    print(root)

post_order(0, len(pre) - 1)
