import math
# 2344ms

# 1. 에라토스테네스의 체로 소수 미리 만듦 (최대값 10000까지)
MAX_N = 10000
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(MAX_N)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False


primes = [i for i in range(2, MAX_N + 1) if is_prime[i]]

T = int(input())

for i in range(T):
    N = int(input())

    # 2. 투 포인터 (시간복잡도 O(N))
    l, r = 0, len(primes) - 1
    ret1, ret2 = 0, 0

    while(l <= r):
        if primes[l] + primes[r] == N:
            ret1, ret2 = primes[l], primes[r] # 갱신
            l += 1
            r -= 1
        elif primes[l] + primes[r] < N:
            l += 1
        else:
            r -= 1
    
    print(ret1, ret2)