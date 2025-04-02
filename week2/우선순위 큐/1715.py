import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(heap, card)

ret = 0

if len(heap) == 1:
    print(0)
else: 
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        heapq.heappush(heap, n1 + n2)
        ret += n1 + n2

    print(ret)
