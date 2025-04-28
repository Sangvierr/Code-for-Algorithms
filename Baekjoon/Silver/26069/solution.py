import sys

T = int(sys.stdin.readline().rstrip())

dance_set = set()
dance_set.add('ChongChong')
records = []

for _ in range(T):
    a, b = sys.stdin.readline().rstrip().split()

    records.append((a, b))

for a, b in records:
    if a in dance_set and b not in dance_set:
        dance_set.add(b)
    elif b in dance_set and a not in dance_set:
        dance_set.add(a)

print(len(dance_set))