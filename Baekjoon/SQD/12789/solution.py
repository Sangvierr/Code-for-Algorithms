T = int(input())
line = list(map(int, input().split()))
stack = []
out = 1

for l in line:
    stack.append(l)
    while stack and stack[-1] == out: # 스택에 뭔가 있고, 맨 위가 현재 나가야 하는 놈이라면
        stack.pop()
        out+=1

if not stack and line:
    print('Nice')
else:
    print('Sad')