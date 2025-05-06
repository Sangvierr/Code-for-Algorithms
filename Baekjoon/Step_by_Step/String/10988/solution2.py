import sys

line = sys.stdin.readline().rstrip()
lst=[]
for l in line:
    lst.append(l)
n=len(lst)
is_palin = 1

for i in range(n):
    if lst[i] != lst[n-1-i]:
        is_palin=0
        break

print(is_palin)