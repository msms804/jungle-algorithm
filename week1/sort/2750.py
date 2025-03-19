N = int(input())
arr = []

# 1. 배열에 push
for i in range(N):
    tmp = int(input())
    arr.append(tmp)

# 2. sorting
arr.sort()

for i in arr:
    print(i)


