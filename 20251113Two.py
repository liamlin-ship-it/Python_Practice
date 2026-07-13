numbers = list(map(int, input().split()))

frequency_map = {}

for num in numbers:
    if num == 0:
        break

    if num in frequency_map:
        frequency_map[num] += 1
    else:
        frequency_map[num] = 1
    
sorted_numbers = sorted(frequency_map.keys())
for num in sorted_numbers:
    print(f"{num} {frequency_map[num]}")