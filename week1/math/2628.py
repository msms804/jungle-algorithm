garo, sero = map(int, input().split())
n = int(input())

a = [0, sero]
b = [0, garo]

for i in range(n):
    x, y = map(int, input().split())

    if x == 0:
        a.append(y)
    elif x == 1:
        b.append(y)

a.sort()
b.sort()

maxWidth = 0
maxHeight = 0
 
for i in range(1, len(a)):
    maxHeight = max(maxHeight, a[i] - a[i - 1])

for i in range(1, len(b)):
    maxWidth = max(maxWidth, b[i] - b[i - 1])

print(maxHeight * maxWidth)

