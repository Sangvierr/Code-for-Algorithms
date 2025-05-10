# 백준 16926번
# 반시계 방향으로 원소를 하나씩 회전시킴
# 배열 자체를 회전시키는 문제와는 다름
# deque를 사용해서 껍데기 벗기듯이 확인
# 상우하좌 방향으로 확인하면서 돌림

from collections import deque

M, N, R = map(int, input().strip().split()) # 행, 열, 회전 수
arr = [list(map(int, input().strip().split())) for _ in range(M)]
result = [[0]*N for _ in range(M)]
q = deque()

for i in range(min(M, N)//2): # 겹겹 하나씩 loop을 돌기
    q.clear()

    # 껍데기 만들기
    up=arr[i][i : N-i]
    right = [arr[row][N-1-i] for row in range(i+1, M-1-i)]
    down=arr[M-1-i][i : N-i][::-1]
    left=[arr[row][i] for row in range(i+1, M-1-i)][::-1]
    
    # 큐에 순서대로 넣기
    q.extend(up)
    q.extend(right) 
    q.extend(down)
    q.extend(left)

    # 회전(반시계는 음수)
    q.rotate(-R)

    # 결과 담기(상 > 우 > 하 > 좌)
    idx = 0
    for j in range(i, N - i):
        result[i][j] = q[idx]
        idx += 1
    for j in range(i + 1, M - 1 - i):
        result[j][N - 1 - i] = q[idx]
        idx += 1
    for j in range(N - 1 - i, i - 1, -1):
        result[M - 1 - i][j] = q[idx]
        idx += 1
    for j in range(M - 1 - i - 1, i, -1):
        result[j][i] = q[idx]
        idx += 1

for row in result:
    print(' '.join(map(str, row)))