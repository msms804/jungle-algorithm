#1110번 더하기 사이클
N = int(input())
res = N
cnt = 0

while(True):
    if N < 10:
        N = str(N)
        N = '0' + N

    N = str(N) # str로 바꿈

    n1 = int(N[0])
    n2 = int(N[1])
    newNum = str(n1 + n2)
    
    if(int(newNum) < 10):
        newNum = '0' + newNum

    N = int(N[1] + newNum[1]) # 새로운 수 만듦

    cnt += 1

    if(res == N): break # 숫자가 같아지면 break

print(cnt)
