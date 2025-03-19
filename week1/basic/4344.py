C = int(input())

for i in range(C):
    arr = map(int, input().split())
    arr = list(arr)

    students = arr[0]
    sum = 0
    more_than_avg = 0

    # 1 부터 끝까지 for문 돌려야
    for i in arr[1: ]:
        sum += i
    
    avg = sum / students

    for i in arr[1: ]:
        if i > avg:
            more_than_avg += 1

    res = (more_than_avg / students) * 100

    print("{:.3f}%".format(res)) 
    
