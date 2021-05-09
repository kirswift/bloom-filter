from filter import Filter
import time

file = open("text.txt", mode="r", encoding="utf-8")

values = file.read().split(' ')

f = Filter(len(values) * 10, len(values))
f.add(values)

words_to_find = ["nonproprietary", "catharsis"]

for x in words_to_find:
    print("\nОпределение наличия методом Блума: ")
    t = time.perf_counter_ns()
    res = f.exists(x)
    res_time = time.perf_counter_ns() - t
    print(f"Слово {x} {'найдено' if res else 'не найдено'}")
    print(f"Операция заняла {res_time} нс")
    print("Определение наличия стандартным методом: ")
    t = time.perf_counter_ns()
    res = False
    for val in values:
        if val == x:
            res = True
    print(f"Слово {x} {'найдено' if res else 'не найдено'}")
    res_time = time.perf_counter_ns() - t
    print(f"Операция заняла {res_time} нс")
