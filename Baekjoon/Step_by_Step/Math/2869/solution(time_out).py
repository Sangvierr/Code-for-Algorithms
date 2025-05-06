import sys

a, b, v = map(int, sys.stdin.readline().rstrip().split())

current = 0
day = 1
while True:
    current += a # 올라가기

    if current >= v: # 올라간 높이가 나무보다 높다면 종료
        break

    current -= b # 떨어지기

    day += 1 # 올라가고 떨어지기 완료하면 하루가 지남

print(day)