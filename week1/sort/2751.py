# https://velog.io/@kr_diosamor/baekjoon18
# 힙정렬로 풀면 시간초과가 안난다고 한다.
import sys

# 입력 개수 받기
N = int(sys.stdin.readline().strip())

# 숫자 리스트 입력받기
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 정렬
arr.sort()

# 출력 최적화
sys.stdout.write("\n".join(map(str, arr)) + "\n")
