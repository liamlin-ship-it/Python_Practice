import math

numbers = [15.6, 12, 84.2, 546, 95.22, 45, 362.21, 555.5, 75.2]

n = int(input())

if 1 <= n <= len(numbers):
    first_n_items = numbers[:n]
    average = sum(first_n_items) / n

    print(round(average, 2))