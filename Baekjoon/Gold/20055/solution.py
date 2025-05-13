# 1. 벨트 회전(로봇도 함께)
# 2. 로봇 이동(뒤에서부터) 
# 3. 로봇 올림
# 끝에 온 놈은 내리기는 계속 수행

N, K = map(int, input().split())
A = list(map(int, input().split())) # 내구도 리스트
occupied = [0] * N # 로봇이 올라가있는지
steps = 0 # 최종 출력 결과

# 오른쪽 방향으로 리스트 회전
def rotate_clockwise(lst):
    return [lst[-1]]+lst[:-1]

while True:
    steps+=1
    
    # 1. 벨트 회전
    A = rotate_clockwise(A)
    occupied = rotate_clockwise(occupied)
    if occupied[N-1]: # 마지막에 있는 애는 바로 내림
        occupied[N-1] = 0

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):
        if occupied[i]:
            if not occupied[i+1] and A[i+1]>0: # 다음 칸 비어있고, 내구도가 0 이상이면
                occupied[i]=0 # 이동
                occupied[i+1]=1 # 도착
                A[i+1]-=1 # 도착하면 내구도 하락

                if i+1==N-1:
                    if occupied[i+1]:# 마지막에 있는 애는 바로 내림
                        occupied[N-1] = 0

    # 3. 로봇 올리기
    if A[0] > 0 and not occupied[0]:
        occupied[0]=1
        A[0]-=1
    
    # 종료 확인
    if A.count(0) >= K:
        print(steps)
        break