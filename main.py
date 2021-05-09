from filter import Filter

file = open("text.txt", mode="r", encoding="utf-8")

values = file.read().split(' ')

f = Filter(len(values) * 10, len(values))
f.add(values)

print(f.exists("woman"))