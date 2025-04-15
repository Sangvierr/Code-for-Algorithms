import sys
N = int(sys.stdin.readline().rstrip())
result=0
num = sys.stdin.readline().rstrip()
for i in range(N):
    result+=int(num[i])
print(result)