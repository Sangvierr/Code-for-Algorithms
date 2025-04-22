import sys

T = int(sys.stdin.readline().rstrip())

cases = []
for _ in range(T):
    cent = int(sys.stdin.readline().rstrip())
    cases.append(cent)

change = [25, 10, 5, 1] # 쿼터, 다임, 니켈, 페니

gives = []
for case in cases:
    give_count = []
    remaining = case
    for c in change:
        count = remaining // c # 잔돈 개수
        give_count.append(count)
        remaining = remaining % c # 남은 금액 업데이트 후, 다음 동전으로 잔돈 개수 계산산
    gives.append(give_count)

for give in gives:
    print(*give)