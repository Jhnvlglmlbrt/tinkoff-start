def parse_config(file):
    stack = [{}] # Инициализируем стек с пустым словарем в качестве первого элемента
    for line in file:
        line = line.strip() # удаляет пробельные символы с начала и конца строки
        if line == '{': # Если строка содержит '{', добавляем копию текущего словаря в стек
            stack.append(stack[-1].copy())
        elif line == '}':  # Если строка содержит '}', удаляем последний словарь из стека
            stack.pop()
        else:
            var, val = line.split('=') # Разделяем строку на имя переменной и значение
            if val.isdigit() or (val[0] == '-' and val[1:].isdigit()): # Если значение является числом или отрицательным числом
                stack[-1][var] = val # Присваиваем переменной значение как строку
            else: # Если значение val не является числом или отрицательным числом
                #print(stack)
                stack[-1][var] = stack[-1].get(val, 0) # Если значение является именем переменной, получаем его значение из текущего словаря или присваиваем 0, если значение отсутствует
                #print(stack)
                # stack[-1]) - доступ к последнему словарю в стеке, те откуда мы будем брать значение (допустим у нас d = a) - стек будет - {'thats': 0, 'a': '10', 'ten': '-10', 'aboba': '10'}
                print(stack[-1][var]) # Выводим значение переменной

with open('config.txt', 'r') as file:
    parse_config(file)