person = input().split(", ")

bmi_list = []

for p in person:
    each_person = p.split("-")

    height = each_person[1]
    weight = each_person[2]

    weight = float(weight)
    height = float(height)

    bmi = weight / ((height / 100) ** 2)

    bmi_list.append([bmi, p])

bmi_list.sort(reverse=True)

result = []

for i in bmi_list:
    result.append(i[1])

print(result)