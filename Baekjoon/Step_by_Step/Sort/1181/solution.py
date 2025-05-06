T = int(input())

char = []
for _ in range(T):
    c = input()
    if c not in char:
        char.append(c)

char.sort(key=lambda item: (len(item), item))

print(*char, sep='\n')