from collections import Counter

# Ввод количества лет, за которые у Ани есть данные
N = int(input())
teams = [input().split() for _ in range(N)]

# Приведение команд к единому формату, сортировка и подсчет повторений
normalized_teams = [tuple(sorted(team)) for team in teams]
team_counts = Counter(normalized_teams)

# Нахождение максимального числа побед команды в одинаковом составе
max_wins = max(team_counts.values())

# Вывод результата
print(max_wins)
