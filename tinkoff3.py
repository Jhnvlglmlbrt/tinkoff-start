n = int(input())  # Число дней
data = list(map(int, input().split()))  # Данные за каждый день

max_profit = 0  # Изначальная максимальная прибыль

for i in range(n-1): # i = 0 -> n = 1, i = 1 -> n = 2
    for j in range(i+1, n): # i + 1 = 2, а значит j превышает допустимый индекс дней, т.к. у нас нет 3 дня, а значит с чем что мы будем менять ведь i = 1 - второй день, а i = 2 - уже третий день
        temp_data = data.copy()  # Создаем временную копию данных
        temp_data[i], temp_data[j] = temp_data[j], temp_data[i]  # Меняем значения двух дней
        profit = sum((-1) ** (k % 2) * temp_data[k] for k in range(n))  # Вычисляем прибыль
        max_profit = max(max_profit, profit)  # Обновляем максимальную прибыль

print(max_profit)
