# 주어진 K개에서 조합 써서 6개 출력하기

def combination(n, nums, new_arr, c):
    total = []
    if len(new_arr) == n:
        total.append(new_arr)
        return total
    
    for i in range(c, len(nums)):
        total.extend(combination(n, arr, new_arr+[nums[i]], i+1))

    return total

num = list(map(int, input().strip().split()))
K = num[0]
arr = num[1:]
result = combination(6, arr, [], 0)
for row in result:
    print(*row)