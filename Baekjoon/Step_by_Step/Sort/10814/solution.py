T = int(input())

lst=[]
for _ in range(T):
    age, name = input().split()
    age=int(age)
    lst.append([age, name])

lst.sort(key=lambda item: (item[0]))

for l in lst:
    print(*l)