import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

mat1 = []
mat2 = []

for i in range(N):
    mat1.extend(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    mat2.extend(map(int, sys.stdin.readline().rstrip().split()))

total = []
for num1, num2 in zip(mat1, mat2):
    total.append(num1+num2)

for i in range(N):
    print(*total[i*M:(i+1)*M])