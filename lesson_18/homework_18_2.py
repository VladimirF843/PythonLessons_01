# --- 1. Функция, возвращающая список в обратном порядке ---

def reversed_list(input_list):
    new_list = []
    i = 0
    list_length = len(input_list)

    while i < list_length:
        new_list.append(input_list[list_length - 1 - i])
        i += 1

    print(f"Список в обратном порядке: {new_list}")
    return new_list


list_numbers = [11, 12, 13, 14, 15]
reversed_list(list_numbers)


# -------------------------------------------------------------------

# --- 2. Итератор четных чисел (Класс) ---

class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


my_iterator = EvenNumbers(32)
print("\nЧетные числа до 32:")
for num in my_iterator:
    print(num)

# -------------------------------------------------------------------

# --- 3. Ручной проход по итератору ---

my_list = [1, 2, 3, 4, 5]
my_iterable = iter(my_list)

print("\nРучной проход по итератору:")
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))

# -------------------------------------------------------------------

# --- 4. Использование enumerate ---

my_list_names = ['яблоко', 'банан', 'вишня']
print("\nИспользование enumerate:")
for index, value in enumerate(my_list_names):
    print(f"Индекс {index}: {value}")