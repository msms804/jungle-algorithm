A, B = input().split()

reversedA = int(A[::-1])
reversedB = int(B[::-1])

if(reversedA > reversedB):
    print(reversedA)
else:
    print(reversedB)
