T = int(input())

stack = []
for _ in range(T):
    line = input().split()

    # 정수가 2개 입력되는 경우
    if len(line) == 2:
        cmd, num = map(int, line)
        if cmd == 1:
            stack.append(num)

    # 정수가 한개만 입력되는 경우
    else:
        num = int(line[0])
        if num == 2:
            # 스택 비어있다면
            if not stack: 
                print(-1)
            else:
                print(stack.pop())
        elif num == 3:
            print(len(stack))
        elif num == 4:
            if not stack:
                print(1)
            else:
                print(0)
        elif num == 5:
            if not stack:
                print(-1)
            else:
                print(stack[-1])