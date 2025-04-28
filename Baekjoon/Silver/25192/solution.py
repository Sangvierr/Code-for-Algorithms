import sys

T = int(sys.stdin.readline())

gom = set()
cnt = 0

for _ in range(T):
    string = sys.stdin.readline().rstrip()

    if string == "ENTER":
        cnt += len(gom)
        gom = set()
    else:
        gom.add(string)

cnt += len(gom)
print(cnt)