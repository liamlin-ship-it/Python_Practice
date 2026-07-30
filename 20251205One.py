data = input().split(", ")

bmi_list = []

for i in range(len(data)):
    parts = data[i].split("-")
    height = float(parts[1]) / 100
    weight = float(parts[2])
    bmi = weight / (height ** 2)
    bmi_list.append((bmi, data[i]))

bmi_list.sort(reverse = True)

final_output = []

for item in bmi_list:
    final_output.append(item[1])

print(final_output)