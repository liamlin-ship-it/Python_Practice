target = int(input())

num = list(map(int, input().split()))

found = False

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] + num[j] == target:
            print(num[i], num[j])
            found = True
            break
    
    if found:
        break