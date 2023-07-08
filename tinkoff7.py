def count_movements(s, queries):
    counts = []

    for l, r in queries:
        subsequence = s[l - 1: r]  # Получаем подстроку с l-го по r-й символы
        unique_chars = set(subsequence)  # Находим уникальные символы в подстроке

        movements = len(unique_chars)  # Количество уникальных символов равно количеству операций второго типа
        #print(movements)


        if l == 1 and r == len(s):
            movements += len(subsequence)  # Добавляем шаги для полного плана супермаркета

        counts.append(movements)

    return counts


# Ввод данных
s = "hello"  # Ввод строки с планом супермаркета
queries = [(1, 5), (1, 2), (2, 5)]  # Ввод границ подотрезков

# Вызов функции и вывод результатов
result = count_movements(s, queries)
for count in result:
    print(count)
