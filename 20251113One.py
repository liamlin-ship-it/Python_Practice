num = list(map(int, input().split()))

a = num[0]
b = num[1]

for i in range(a):
    for j in range(b):
        print("*", end="")

    print()