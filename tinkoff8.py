def count_matching_domains(domains, queries):
    results = []

    for query in queries:
        count = 0

        prefix, suffix = query
        print(prefix, " prefix", suffix, " suffix")

        for domain in domains:
            #print(domain, " domain")
            if domain.startswith(prefix) and domain.endswith(suffix):
                count += 1

        results.append(count)

    return results


# Ввод данных
n, m = map(int, input().split())  # Ввод количества закупленных доменов и покупателей

domains = []
for _ in range(n):
    domain = input().strip()  # Ввод закупленного домена
    domains.append(domain)

queries = []
for _ in range(m):
    prefix, suffix = input().split()  # Ввод запроса покупателя
    queries.append((prefix, suffix))

# Вызов функции и вывод результатов
result = count_matching_domains(domains, queries)
for count in result:
    print(count)
