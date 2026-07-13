rangeToCheck = int(input())

numbers = list(map(int, input().split()))

count = 0
calculate = 0

for num in numbers:
    if num % 2 == 0:
        count += 1
        calculate += num

    if count == rangeToCheck:
        break

print(calculate)
