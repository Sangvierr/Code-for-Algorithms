# 하루에 a-b만큼 오른다.
# 마지막 날에는 최소 v-a만큼 와있다. 
# 그래서 a만큼 오르면 도착
# 따라서 (v-a) // (a-b) + 1을 하면 마지막 날까지 오르는데 며칠 걸렸는지 알 수 있음
# 거기서 +1하면 d-day 날짜가 나옴옴

import sys

a, b, v = map(int, sys.stdin.readline().rstrip().split())

if a > v:
    print(1)
else:
    if (v-a) % (a-b) == 0: # 나눠떨어지면 ceiling할 필요가 없어서 1만 더함
        dday = ((v-a) // (a-b)) + 1
    else:
        dday = ((v-a) // (a-b)) + 2
print(dday)