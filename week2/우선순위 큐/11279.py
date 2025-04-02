import heapq
import sys
# heapq는 최소힙, 그래서 최대힙으로 쓰려면 음수로 변환해서 푸시한다
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())

    # x가 자연수라면 
    # 자연수가 2^31보다 작다 -> 매우 크므로 입력 바꿔야
    if x:
        heapq.heappush(heap, -x)
    # x가 0이라면 배열에서 가장 큰 값 출력, 그 값 제거
    else:
        if heap:
            tmp = heapq.heappop(heap)
            print(-tmp)
        else:
            print("0")
