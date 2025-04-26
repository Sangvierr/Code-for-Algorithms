N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input())

cnt = []
for a in range(N-7):
    for b in range(M-7):
        idx1=0 # 'W'와 다른거 count
        idx2=0 # 'B'와 다른거 count
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 두 인덱스의 합이 짝수라면 0, 0과 같아야 함
                    if arr[i][j] != 'W':
                        idx1 += 1
                    if arr[i][j] != 'B':
                        idx2 += 1
                else: # 두 인덱스의 합이 홀수라면, 0, 0과 달라야 함
                    if arr[i][j] != 'W':
                        idx2 += 1
                    if arr[i][j] != 'B':
                        idx1 += 1

        cnt.append(min(idx1, idx2))

print(min(cnt))