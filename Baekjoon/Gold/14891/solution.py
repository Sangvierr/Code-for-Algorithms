# 맞닿아 있는 극이 다르면 반대방향으로 회전
# 맞닿아 있는 극이 같으면 회전 안 함
# 연쇄적으로 회전해야 하기 때문에 if-else로 케이스를 나눌 수 없음
# 이를 위해 좌측으로 가다가 0이 되면 종료되는 while 문 + 오른쪽으로 가다가 4가 되기 전에 종료되는 while 문
# 회전방향도 연쇄적으로 바뀜

# 톱니 4개, 12시부터 시계방향으로 8개
# 인덱싱을 위해 하나의 리스트로 관리
total = [list(map(int, input())) for _ in range(4)] # 1이면 S극

rotate=[]
R = int(input()) # 회전 횟수
for _ in range(R):
    topni, direction = map(int, input().strip().split()) # 회전시킨 톱니, 방향(1이 시계, -1이 반시계)
    rotate.append((topni, direction))

def rotate_clock(lst):
    return [lst[-1]] + lst[:-1]

def rotate_counterclock(lst):
    return lst[1:]+[lst[0]]

# 1번의 인덱스 2 - 2번의 인덱스 6
# 2번의 인덱스 2 - 3번의 인덱스 6
# 3번의 인덱스 2 - 4번의 인덱스 6

for topni, direction in rotate:
    topni_idx=topni-1

    to_rotate = [(topni_idx, direction)] # 회전해야 하는 톱니

    # 왼쪽을 연쇄 회전(왼쪽의 오른쪽을 확인한다면 끝으로 가도 인덱스 넘칠 일 없음, 반대도 동일)
    left_idx=topni_idx-1
    ld=-direction
    while left_idx >= 0:
        # 현재와 그 오른쪽의 극이 다르다면 => 반대로 움직임
        if total[left_idx][2] != total[left_idx+1][6]:
            to_rotate.append((left_idx, ld))
            ld=-ld
            left_idx-=1
        # 극이 같다면 => 안 움직임
        else:
            break

    # 오른쪽 연쇄 회전
    right_idx=topni_idx+1
    rd=-direction
    while right_idx < 4:
        # 현재와 그 왼쪽의 극이 다르다면 => 반대로 움직임
        if total[right_idx-1][2] != total[right_idx][6]:
            to_rotate.append((right_idx, rd))
            rd=-rd
            right_idx += 1
        # 극이 같다면 => 안 움직임
        else:
            break

    # 실제로 움직이기
    for idx, direction2 in to_rotate:
        if direction2 == 1:
            total[idx] = rotate_clock(total[idx])
        else:
            total[idx] = rotate_counterclock(total[idx])

score=0
for i in range(4):
    if total[i][0] == 1:
        score+=2**i
print(score)