numbers = list(map(int, input().split()))

current_length = 1
max_length = 0
best_start = -1
best_end = -1

prev_trend = 0

for i in range(1, 20):
    if numbers[i] > numbers[i - 1]:
        curr_trend = 1
    elif numbers[i] < numbers[i - 1]:
        curr_trend = -1
    else:
        curr_trend = 0

    if curr_trend != 0 and curr_trend != prev_trend:
        current_length += 1
    else:
        if curr_trend != 0:
            current_length = 2
        else:
            current_length = 1

    if current_length >= 3 and current_length > max_length:
        max_length = current_length
        best_end = i
        best_start = i - current_length + 1

    prev_trend = curr_trend
    
if max_length >= 3:
    print(f"{best_start} {best_end}")
else:
    print("-1 -1")