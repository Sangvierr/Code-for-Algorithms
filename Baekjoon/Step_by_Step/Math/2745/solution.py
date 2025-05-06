# B진법인 N을 10진법으로 변환
# for문을 돌면서 각 숫자or알파벳을 확인
# 숫자: digit-i-1의 제곱을 곱함
# 알파벳: 알파벳을 아스키코드로 변환하고, digit-i-1의 제곱을 곱함
# A는 아스키 코드로 65임
# 참고: https://ghi512.tistory.com/93

import sys

N, B = sys.stdin.readline().rstrip().split()

digit = len(N)
B = int(B)
result = 0

for i in range(digit):
    w = N[i]

    if 'A' <= w <= 'Z':
        result += int(ord(w)-55) * (B**(digit-i-1))
    else:
        result += int(w) * (B**(digit-i-1))

print(result)