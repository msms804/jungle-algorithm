import sys
# 괄호의 값

str = list(sys.stdin.readline().strip())
stack = []
# [][]((])
for c in str:
    if c == '(':
        stack.append(c)
    elif c == ')':
        tmp = 0
        # 스택이 비어있지 않고 스택의 top이 ( 가 아닌 경우
        while stack and stack[-1] != '(':
            # 숫자가 아닌경우 예외처리 해야
            tmp += stack.pop()

        # stack 이 있고 짝이 맞는 경우
        if stack and stack[-1] == '(':
            stack.pop()
            if tmp == 0:
                stack.append(2)
            else:
                stack.append(2 * tmp)
        

    elif c == '[':
        stack.append(c)
        
    elif c == ']':
        tmp = 0

        while stack and stack[-1] != '[':
            # 숫자가 아닌경우 예외처리 해야
            
            tmp += stack.pop()

        if stack and stack[-1] == '[':
            stack.pop()
            if tmp == 0:
                stack.append(3)
            else:
                stack.append(3 * tmp)


for s in stack:
    if not isinstance(s, int):
        print(0)
        sys.exit(0)

print(sum(stack))
