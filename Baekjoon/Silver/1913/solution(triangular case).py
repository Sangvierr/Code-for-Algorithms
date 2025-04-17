import sys

n = int(sys.stdin.readline().rstrip())

lst = [[0]*i for i in range(1, n+1)]

dir_guide = [(1, 1), (0, -1), (-1, 0)] # 대각 > 좌 > 상
dir_idx = 0
x, y = 0, 0 # 현재 위치
lst[0][0]=1

total = n*(n+1)//2

for i in range(2, total+1):
    dx, dy = dir_guide[dir_idx]
    next_x, next_y = x+dx, y+dy
    
    # 다음 디렉션이 갈 수 있는 방향인지
    if 0 <= next_x < n and 0 <= next_y < n and lst[next_x][next_y] == 0:
        x, y = next_x, next_y
        lst[x][y] = i%10
    
    # 갈 수 없다면
    else:
        dir_idx = (dir_idx+1)%3
        dx, dy = dir_guide[dir_idx]
        x, y = x+dx, y+dy
        lst[x][y]=i%10
    
for row in lst:
    print(' '.join(map(str, row)))
        