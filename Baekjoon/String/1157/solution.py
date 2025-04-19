import sys

line = sys.stdin.readline().rstrip()

lst = []
for l in line:
    lst.append(l.upper())

cnt_dict = {}
for char in lst:
    if char in cnt_dict:
        cnt_dict[char] += 1
    else:
        cnt_dict[char] = 1

max_cnt=0
most_common = []

for char, count in cnt_dict.items():
    if count > max_cnt:
        most_common = [char]
        max_cnt = count
    elif count == max_cnt:
        most_common.append(char)
    else:
        continue

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])
