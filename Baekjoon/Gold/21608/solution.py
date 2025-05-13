# 채우는 방향 우선순위: 상좌우하
# 1. BFS/달팽이랑 비슷하게 주변에 좋아하는 애 몇명인지 -> 빈 자리 몇개인지 -> 상좌우하
# 2. 비어있는 칸을 모두 돌며 가장 좋아하는 애가 많은 곳을 탐색 -> 저장/정렬/인덱싱

N = int(input())
students = [list(map(int, input().strip().split())) for _ in range(N**2)] # 애들이 누구 좋아하는지 정보
grid = [[0]*N for _ in range(N)] # 이제 채워야 하는 배열
dir_guide=[(-1, 0), (0, -1), (0, 1), (1, 0)] # 상좌우하

for student in students:
    available=[]

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0: # 그리드의 빈자리를 대상으로 선호도 탐색

                # 주위에 좋아하는 학생 몇명 있는지 탐색
                prefer, empty = 0, 0
                for dr, dc in dir_guide:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<N and 0<=nc<N:
                        if grid[nr][nc] in student[1:]:
                            prefer+=1
                        if grid[nr][nc] == 0:
                            empty+=1
                # 탐색 완료
                available.append((r, c, prefer, empty)) # 행, 열, 좋아하는 학생 몇명, 비어있는거 몇개

    # 각 학생마다 좋아하는 애 몇명인지 -> 빈 자리 몇개인지 -> 상좌우하 순으로 정렬 (sort는 기본 오름차순)
    available.sort(key=lambda item: (-item[2], -item[3], item[0], item[2]))
    grid[available[0][0]][available[0][1]] = student[0]

#print(grid)

students.sort() # 1, 2, 3 순으로 만들어야 함
#print(students)
answer=0
score = [0, 1, 10, 100, 1000]
for r in range(N):
    for c in range(N):
        cnt=0

        for dr, dc in dir_guide:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] in students[grid[r][c]-1]:
                    cnt+=1

        answer+=score[cnt]

print(answer)