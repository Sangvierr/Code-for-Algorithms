# 홀수 N이 주어짐
# 정사각형의 정중앙에서 시작
# 회오리 모양으로 정중앙부터 회오리 모양으로 외부로 나감
# 상, 우, 하, 좌 방향으로 움직임
# 움직이는 칸수가 2번씩 반복됨

N = int(input()) # 한 변의 길이
target = int(input()) # 찾고자 하는 수

arr = [[0]*N for _ in range(N)]
r, c = (N-1)//2, (N-1)//2 # 정중앙
arr[r][c] = 1 # 시작점은 1
move = 1 # 2번마다 1씩 증가시키면서 칸 이동
target_r, target_c = -1, -1 # 찾고자 하는 수 초기화
dir_guide = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌
dir_idx = 0 # # 먼저 위로 가다가 못 가면 다음 인덱스로 넘기는 용
num=2 # 채워 넣을 숫자

# 탐색
while num <= N**2: # 안에서 2번씩 이동하는 부분이 있기 때문에 for문보다는 while로 넣어주는 숫자가 최종숫자일때까지 반복하는게 좋음
    for _ in range(2): # 2번씩 이동
        for _ in range(move): # 처음은 한칸 이동, 2번 뒤에는 2칸, ...
            dr, dc = dir_guide[dir_idx]
            r=r+dr
            c=c+dc

            # 갈 수 있는지?
            if 0<=r<N and 0<=c<N:
                arr[r][c]=num

                # 넣은 숫자가 찾는 숫자인지?
                if num == target:
                    target_r, target_c = r+1, c+1
                num+=1
                
        dir_idx=(dir_idx+1)%4
    move+=1

for row in arr:
    print(' '.join(map(str, row)))

if target == 1:
    print(N//2+1, N//2+1)
else:
    print(target_r, target_c)