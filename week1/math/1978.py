# 왜이리 헷갈리지.. 다시 해볼것
import math
# 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력
N = int(input())

nums = map(int, input().split())
nums = list(nums)

prime_count = 0
for num in nums: # 각 요소는 1000 이하의 자연수
    if num == 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: # 나누어 떨어지면 소수 아님
            is_prime = False
            break
    if is_prime:
        prime_count += 1


print(prime_count)
