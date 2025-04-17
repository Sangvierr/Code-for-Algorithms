import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

lst = [[0]*n for _ in range(n)]

dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 > 우 > 하 > 좌
dir_idx = 0
x, y = (n-1)//2, (n-1)//2 # 첫 시작은 중앙
lst[x][y] = 1 # 첫 시작은 1
length=1
tx, ty = x, y # 정답 출력용 변수
num=2

while num <= n**2:
    for _ in range(2): # 상우하좌 칸수를 2번씩 반복
        for _ in range(length): # 1, 1, 2, 2, 3, 3 ... 같은 식으로 이동
            dx, dy = dir_guide[dir_idx]
            x, y = x+dx, y+dy
            
            # 지금 가려는 방향이 갈 수 있는 방향임
            if 0<=x<n and 0<=y<n:
                lst[x][y]=num
                
                if num == m:
                    tx, ty = x, y
                num+=1
                
        dir_idx=(dir_idx+1)%4
    length+=1
        
for row in lst:
    print(' '.join(map(str, row)))

if m == 1:
    print((n-1)//2+1, (n-1)//2+1)
else:
    print(tx+1, ty+1)