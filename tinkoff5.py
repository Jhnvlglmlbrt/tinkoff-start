import re

inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

workers = []
requests = []

for _ in range(n):
    workers.append(input())
    #print(workers)

for _ in range(m):
    req = input().split(' ')
    requests.append((int(req[0]),req[1]))
    #print(requests)

# Вывод списка работников
print("Исходный список работников по порядку добавления:")
for i, worker in enumerate(workers, start=1):
    print(i, worker)

print("")

for request in requests:
    k, prefix = request
    workers_with_prefix = list(filter(lambda x: re.match(prefix, x), workers))
    workers_with_prefix.sort()
    if k <= len(workers_with_prefix):
        print(f"Отфильтрованный и отсортированный результат для запроса ({k}, {prefix}):")
        for i, worker in enumerate(workers_with_prefix, start=1):
            print(i, worker)
        print("Итоговый результат:", workers.index(workers_with_prefix[k - 1]) + 1, " в исходном наборе")
    else:
        print(f"Результат для запроса ({k}, {prefix}):")
        print("Нет подходящих работников")
    print("")

# Вывод списка работников
print("Список работников:")
for i, worker in enumerate(workers, start=1):
    print(i, worker)