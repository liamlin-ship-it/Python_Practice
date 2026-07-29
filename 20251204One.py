words = input()

name = words.split("@")[0]

provider = words.split("@")[1].split(".")[0]

extension = words.split("@")[1].split(".")[1]

print(name)
print(provider)
print(extension)