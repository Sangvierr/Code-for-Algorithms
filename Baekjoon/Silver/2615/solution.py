import sys

lst=[]
for _ in range(19):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

dir_guide=[(1, 0), (0, 1), (1, 1), (-1, 1)]
result = 0

for i in range(19):
    for j in range(19):
        if lst[i][j] != 0: # 만약 숫자가 있는 칸이라면
            color = lst[i][j] # 1은 검정, 2는 흰색

            for dx, dy in dir_guide:
                nx, ny, cnt = i+dx, j+dy, 1

                while 0<=nx<19 and 0<=ny<19 and lst[nx][ny] == color: # 유효 범위 안에 있고, 이전과 색이 같음
                    cnt += 1

                    if cnt == 5: # 오목이 되어도 육목이 되면 안됨 + 승리 결과과
                        if 0<=nx+dx<19 and 0<=ny+dy<19 and lst[nx+dx][ny+dy] == color: # 만약 앞 방향에도 같은 색이 있다면 육목
                            break
                        if 0<=i-dx<19 and 0<=j-dy<19 and lst[i-dx][j-dy] == color: # 첫 시작점 이전에도 같은 색이 있다면 육목
                            break

                        if color == 1:
                            result = 1 # 검은색 승리
                        if color == 2:
                            result = 2
                        
                        x, y = i, j # 인덱스 출력용 저장장
                    
                    # 위에서 이동 가능한지 확인함, 실제로 이동
                    nx+=dx
                    ny+=dy

if result > 0:
    print(result)
    print(x+1, y+1)
else:
    print(0)