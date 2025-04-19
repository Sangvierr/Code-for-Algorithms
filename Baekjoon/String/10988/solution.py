import sys

line = sys.stdin.readline().rstrip()

lst = []

for l in line:
    lst.append(l)

n = len(lst)

cnt=0
for i in range(n):
    if i == n//2:
        break
    else:
        if lst[i] == lst[n-1-i]:
            cnt+=1

if cnt == n//2:
    print(1)
else:
    print(0)
