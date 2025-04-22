import sys

N, P = map(int, sys.stdin.readline().rstrip().split())

lst=[]
rest=N

while True:
    rest = (rest*N)%P

    if rest in lst:
        print(len(lst)-lst.index(rest))
        break

    lst.append(rest)