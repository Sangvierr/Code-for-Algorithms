import sys

lst=[]
for _ in range(5):
    lst.append(sys.stdin.readline().rstrip())

# 입력 받은 문자열의 최대 길이를 기준으로 하기 위해 탐색
max_len = 0
for l in lst:
    if len(l) > max_len:
        max_len = len(l)
        
for i in range(max_len):
    for j in range(5):
        if i < len(lst[j]):
            print(lst[j][i], end='')