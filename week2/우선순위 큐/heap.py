import heapq
# 빈 리스트를 만들고, 이를 힙으로 사용
heap = []

# 삽입
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 4)
heapq.heappush(heap, 5)
print("힙에 삽입된 값:", heap)  # 힙 상태 출력

min_value = heapq.heappop(heap)
print("삭제된 최소값:", min_value)
print("힙에 남은 값:", heap)