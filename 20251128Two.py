num = list(map(int, input().split()))

a = num[0]
b = num[1]

for i in range(a):
    for j in range(1, b + 1):
        print("*" * j)

    for j in range(b - 1, 0, -1):
        print("*" * j)

    if i < a - 1:
        print()