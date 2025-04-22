import sys

D, K = map(int, sys.stdin.readline().split())

a_seq = [1, 0]
b_seq = [0, 1]

for i in range(2, D):
    a_seq.append(a_seq[i-1] + a_seq[i-2])
    b_seq.append(b_seq[i-1] + b_seq[i-2])

A = a_seq[D-1]
B = b_seq[D-1]

# 이제 K = A*a + B*b 를 만족하는 정수 a, b를 찾자
for a in range(1, K):
    rest = K - A * a
    if rest % B == 0:
        b = rest // B
        print(a)
        print(b)
        break
