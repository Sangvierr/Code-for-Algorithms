T = int(input())

lst = []
for _ in range(T):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda item : (item[1], item[0]))

for l in lst:
    print(*l)