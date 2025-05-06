from collections import deque

N, M = map(int, input().strip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().split())))
dice = [0, 1, 2, 3] # 0: dummy, 1: top, 2: front, 3: right. bottom=7-top, back=7-front, left=7-right
r, c = 0, 0 # 초기 위치
direction = 1 # 0: 상, 1: 우, 2: 하, 3: 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
total_score = 0

def bfs(row, col, visited):
    q = deque([(row, col)])
    visited[row][col] = True
    connected_sum = 0
    value = board[row][col]

    while q:
        curr_r, curr_c = q.popleft()
        connected_sum += value
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] == value:
                visited[nr][nc] = True
                q.append((nr, nc))
    return connected_sum

def roll_dice(d):
    global dice
    new_dice = [0] * 4
    if d == 0: # 상 (top -> back, back -> bottom, bottom -> front, front -> top)
        new_dice[1] = 7 - dice[2]
        new_dice[2] = dice[1]
        new_dice[3] = dice[3]
    elif d == 1: # 우 (top -> left, left -> bottom, bottom -> right, right -> top)
        new_dice[1] = dice[3]
        new_dice[2] = dice[2]
        new_dice[3] = 7 - dice[1]
    elif d == 2: # 하 (top -> front, front -> bottom, bottom -> back, back -> top)
        new_dice[1] = dice[2]
        new_dice[2] = 7 - dice[1]
        new_dice[3] = dice[3]
    elif d == 3: # 좌 (top -> right, right -> bottom, bottom -> left, left -> top)
        new_dice[1] = 7 - dice[3]
        new_dice[2] = dice[2]
        new_dice[3] = dice[1]
    dice[1], dice[2], dice[3] = new_dice[1], new_dice[2], new_dice[3]

def move():
    global r, c, direction, total_score, dice

    nr, nc = r + dr[direction], c + dc[direction]

    if not (0 <= nr < N and 0 <= nc < N):
        direction = (direction + 2) % 4
        nr, nc = r + dr[direction], c + dc[direction]

    roll_dice(direction)
    r, c = nr, nc

    visited = [[False] * N for _ in range(N)]
    current_score = bfs(r, c, visited)
    total_score += current_score

    bottom_dice = 7 - dice[1]
    board_value = board[r][c]

    if bottom_dice > board_value:
        direction = (direction + 1) % 4
    elif bottom_dice < board_value:
        direction = (direction - 1 + 4) % 4

for _ in range(M):
    move()

print(total_score)