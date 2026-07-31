data = input().split(", ")

data.sort(
    key = lambda person: float(person.split("-")[2]) / ((float(person.split("-")[1]) / 100) ** 2),
    reverse = True
)

print(data)