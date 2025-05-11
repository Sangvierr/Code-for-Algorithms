N = int(input()) # 옷장 개수
o1, o2 = map(int, input().strip().split()) # 열려 있는 옷장 2개
T = int(input()) # 사용할 옷장 개수
arr=[int(input()) for _ in range(T)] # 사용할 벽장의 번호

answer = float('inf') # 문 이동 횟수
def backtracking(o1, o2, s, idx):
    '''
    o1: 현재 문 열린 옷장(가장 왼쪽부터)
    o2: 현재 문 열린 옷장(그 다음)
    s: 현재까지 문 연 횟수
    idx: 현재 arr의 인덱스
    '''

    global answer

    # 종료조건
    if idx == T:
        answer = min(answer, s)
        return

    # 현재까지의 이동 횟수가 최적해보다 크면 탐색 종료
    if answer < s: return

    # 이번에 열어야 할 옷장
    target = arr[idx]

    backtracking(target, o2, s+abs(target-o1), idx+1) # o1을 갔으니깐 칸 수 만큼 더함
    backtracking(o1, target, s+abs(target-o2), idx+1) # o2을 갔으니깐 칸 수 만큼 더함

backtracking(o1, o2, 0, 0)
print(answer)