first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(set(first_result)))
first_1 = [len(x) for x in first]
second_1 = [len(x) for x in second]
third = (first_1[x] <= second_1[y] for x in range(len(first_1)) for y in range(len(second_1)) if x == y)
print(list(third))
