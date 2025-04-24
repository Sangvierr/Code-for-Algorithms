import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0
result = 666

# 모든 수 조합을 탐색
while True:
    if '666' in str(result):
        cnt += 1
    
    if cnt == N:
        break

    result += 1

print(result)