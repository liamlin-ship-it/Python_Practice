numbers = list(map(int, input().split()))

largest = float('-inf')
secomd_largest = float('-inf')

for num in numbers:
    if num > largest:
        secomd_largest = largest
        largest = num
    elif num > secomd_largest and num != largest:
        secomd_largest = num

print(secomd_largest)
