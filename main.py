from filter import Filter

values = ["cat", "dog", "bird", "god", "gosha", "big", "floppa", "russian", "kit", "choppa"]

f = Filter(len(values) * 10, len(values))

f.add(values)

print(f.exists("gosha"))