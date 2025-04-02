from itertools import combinations

N, S = map(int, input().split())

arr = list(map(int, input().split()))
# 1. 조합

# 2. 비트마스킹?

# 3. 백트래킹

res = 0

for i in range(1, len(arr) + 1):
    combi = list(combinations(arr, i))
    
    for c in combi:
        total = 0
        total += sum(c)
        if total == S:
            res += 1


print(res)