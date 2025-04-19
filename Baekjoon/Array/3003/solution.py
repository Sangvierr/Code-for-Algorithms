import sys

num = sys.stdin.readline().rstrip().split()
now = []
for n in num:
    now.append(int(n))

should = [1, 1, 2, 2, 2, 8] # 킹, 퀸, 룩, 비숍, 나이트, 폰

result=[]
for item1, item2 in zip(should, now):
    if item1 == item2:
        result.append(0)
    else:
        result.append(item1-item2)

print(*result)