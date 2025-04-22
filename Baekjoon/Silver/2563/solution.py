import sys

# 100x100 크기의 종이를 1 단위로 채워 나가기
paper = [[0]*100 for _ in range(100)]

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if i > 100 or j > 100:
                break
            paper[i][j] = 1

sum=0
for row in paper:
    sum+=row.count(1)

print(sum)