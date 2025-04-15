import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = sys.stdin.readline().rstrip()

for a in alphabet:
    if a in s:
        print(s.index(a), end=' ')
    else:
        print(-1, end=' ')