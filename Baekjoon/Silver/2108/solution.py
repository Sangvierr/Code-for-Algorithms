import sys

T = int(sys.stdin.readline().rstrip())

lst = []
for _ in range(T):
    num = int(sys.stdin.readline().rstrip())
    lst.append(num)
lst.sort()

n = len(lst)

# 평균
mean = round(sum(lst)/n)

# 중앙값
if n % 2 != 0:
    median = lst[n//2]
else:
    median = (lst[n//2-1] + lst[n//2])/2

# 최빈값
freq = {}
for l in lst:
    if l in freq:
        freq[l] += 1
    else:
        freq[l] = 1

sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
max_freq = sorted_freq[0][1]
modes = [item for item, count in sorted_freq if count == max_freq]
if len(modes) == 1:
    mode = modes[0]
else:
    sorted_modes = sorted(modes)
    mode = sorted_modes[1]

# 범위
ran = lst[-1]-lst[0]

print(mean)
print(median)
print(mode)
print(ran)