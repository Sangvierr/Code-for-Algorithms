# 0과 1로 이뤄진 2차원 배열이 주어짐
# 1이 바닥까지 하강
# 테트리스처럼 바닥부터 1이 쌓이기

m, n = map(int, input().strip().split()) # 행, 열 개수
arr = [list(map(int, input().strip().split())) for _ in range(m)]

def gravity(arr):
    m=len(arr) # 행
    n=len(arr[0]) # 열

    for c in range(n):
        for r in range(m-1, -1, -1): # 맨 밑에서부터 올라옴
            if arr[r][c] == 1: # 현재 위치가 1이라면
                temp_r = r
                while temp_r + 1 < m and arr[temp_r+1][c] == 0: # 하나씩 위로 올라가며 확인
                    arr[temp_r][c]=0 # 먼저 현재 위치를 0으로 만듦
                    temp_r+=1
                    arr[temp_r][c]=1 # 다음 행을 1로 갱신

    return arr

print('중력 적용 전')
for row in arr:
    print(' '.join(map(str, row)))

print('중력 적용 후')
result = gravity(arr)
for row in result:
    print(' '.join(map(str, row)))