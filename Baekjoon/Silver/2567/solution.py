import sys

T = int(sys.stdin.readline().rstrip())

paper=[[0]*101 for _ in range(101)]

# 먼저 사각형 넓이만큼 채우기
for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if i > 100 or j > 100:
               break
            paper[i][j] = 1

# (1, 0), (0, 1), (-1, 0), (0, -1)이면 경계
answer=0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if paper[i+x][j+y] == 0:
                    answer+=1

print(answer)