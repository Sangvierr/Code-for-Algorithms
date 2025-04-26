import sys

K = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(K):
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        if stack:
            stack.pop()
        else:
            continue
    else:
        stack.append(N)

print(sum(stack))