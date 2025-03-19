# 달팽이
A, B, V = map(int, input().split())

days = (V - A) // (A - B) # 며칠 걸렸는지
left = (V - A) % (A - B) 

if left == 0: # 나누어 떨어진다면
    print(days + 1)
else:
    print(days + (left + A) // A + 1)