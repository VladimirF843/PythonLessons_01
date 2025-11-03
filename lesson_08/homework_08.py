def calculate_sum(strings):
    summa = 0

    elements =  strings.split(',')

    try:
        for item in elements:
            number = int(item)
            summa += number

    except ValueError:
        return "Не можу це зробити!"
    return summa


massiv = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "100", "5,-2,7", "1,2,a,4"]

# Обработка и вывод
print("-Результат обработки-")
for string_item in massiv:
    result = calculate_sum(string_item)
    print(f' Строчка: "{string_item}" -> Сума: {result}')