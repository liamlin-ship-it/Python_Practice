nums = list(map(int, input().split()))

total_sum = 0
count = 0

for n in nums:
    total_sum += n
    count += 1

    if total_sum == 0:
        break

print(count)