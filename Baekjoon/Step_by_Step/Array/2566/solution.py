import sys

max_val=-1 # 모든 입력값이 0인 경우를 대비
col_idx=0
row_idx=0

for i in range(1, 10):
    line = map(int, sys.stdin.readline().rstrip().split())
    for j, val in enumerate(line):
        if val > max_val:
            max_val = val
            col_idx = j+1
            row_idx = i

print(max_val)
print(row_idx, col_idx)