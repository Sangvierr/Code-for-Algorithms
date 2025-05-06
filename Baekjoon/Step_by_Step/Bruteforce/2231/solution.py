import sys

N = int(sys.stdin.readline().rstrip())

min_gen = 0

for i in range(1, N+1):
    str_i = str(i)
    digit_sum = sum(map(int, str_i))

    if digit_sum+i == N:
        min_gen = i
        break

print(min_gen)