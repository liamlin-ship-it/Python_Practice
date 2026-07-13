numbers = list(map(int, input().split()))

total = 0

for num in numbers:
    if num < total:
        print(num)
        break
    else:
        total += num