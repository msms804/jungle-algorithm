import sys
import heapq
# https://seongonion.tistory.com/90

N = int(sys.stdin.readline())
max_h = []
min_h = []

for i in range(N):
    n = int(sys.stdin.readline())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -n)
    else:
        heapq.heappush(min_h, n)
    # print("최대힙 : ", max_h)
    # print("최소힙 : ", min_h)
    if max_h and min_h and (-max_h[0] > min_h[0]):
        p1 = -heapq.heappop(max_h)
        p2 = heapq.heappop(min_h)
        
        heapq.heappush(min_h, p1)
        heapq.heappush(max_h, -p2)

    print(-max_h[0])
    # print("-------------")

