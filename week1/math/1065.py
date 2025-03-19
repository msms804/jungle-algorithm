# 한수

N = int(input())
ret = 0


if N < 100: # 두자리수 인 경우
    ret += N
else: # 세자리수인 경우
    ret = 99
    # 1. 세자리수 -> 배열
    strN = str(N)

    # 2. 두번째요소와 첫번째 요소의 차이 구한다
    diff = int(strN[1]) - int(strN[0])

    # not hansu
    
    # 3. for문 돌면서 (이거 함수로 빼도 되지 않나)
    for i in range(100, N + 1):
        hansu = True
        i = str(i)
        for j in range(len(i) - 1):
            if int(strN[j + 1]) - int(strN[j]) != diff:
                hansu = False
                break
            else:
                print("한수 아님", i)
        if hansu:
            ret += 1
        
    
    print("한수의 개수 : ", ret)

    # 4. 만약 하나라도 다르다면 한수 x , break
