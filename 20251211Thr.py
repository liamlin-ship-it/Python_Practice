num = list(map(int, input().split()))

max = num.index(max(num))
min = num.index(min(num))

num[max], num[min] = num[min], num[max]

# the * operator unpacks the list and prints it with spaces
print(*num)