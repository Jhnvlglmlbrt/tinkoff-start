def max_lift_chain(lifts):
    n = len(lifts)
    lifts.sort()  # Сортировка лифтов по возрастанию нижних этажей
    print(lifts)
    dp = [1] * n  # Инициализация массива dp
    prev = [-1] * n  # Массив для хранения предыдущего лифта в цепи
    max_length = 1
    max_index = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if lifts[i][1] == lifts[j][0]:
                # Проверка условия, что лифт не был использован ранее
                # print(i)
                # print(j)
                if lifts[i] != lifts[j]:
                    # print(i)
                    # print(lifts[i])
                    # print(j)
                    # print(lifts[j])

                    dp[j] = dp[i] + 1
                    prev[j] = i  # Сохранение связи что предыдущим лифтом для текущего лифта j является лифт с индексом i
                    #print(prev)

                    max_length = max(dp)
                    #print(dp)
                # else:
                    # print(lifts[j])


    chains = []
    for i in range(n):
        chain = []
        current_index = i
        while current_index != -1:
            chain.append(lifts[current_index])
            current_index = prev[current_index]
        # print(chain)
        #print(current_index)
        chain.reverse()
        chains.append(chain)
    #print(chains)

    return max_length, chains


# Ваш входной список лифтов
lifts = [(2, 6), (5, 6), (2, 5), (2, 2), (6, 8), (2, 2), (0, 2)]

# Вызов функции и получение результата
result_length, result_chains = max_lift_chain(lifts)

# Печать результатов
print("Максимальная длина цепи:", result_length)
print("Цепи лифтов:")
for i, chain in enumerate(result_chains, start=1):
    print(f"Цепь {i}:")
    for lift in chain:
        print(lift)
    print()