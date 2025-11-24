# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result < 25:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_2(num1,num2):
    sum = num1+num2
    return (sum)
print(sum_of_2(100, 100))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    sum1 = 0
    if not numbers:  # проверка на пустой список
        return 0
    for i in numbers:
        sum1 += i
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_lst(list_01):
    rev_list = []
    for i in range(len(list_01) - 1, -1, -1):
        rev_list.append(list_01[i])
    return rev_list
print(reverse_lst([1,2,4,5,6,7]))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(word_list):
    if not word_list:
        return None
    longest_word = word_list[0]
    for word in word_list[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def find_strings_in_list(lst1):
    lst2 = []
    for i in lst1:
        if type(i)==str:
            lst2.append(i)

    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(find_strings_in_list(lst1))

# task 8
def sum_even_elements(lst): # сумма целых чисел

  summa = 0
  for i in lst:
    if i % 2 == 0:
      summa = summa + i
  return summa

# Пример такой:
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_elements(lst1)
print(result) # Виведет: 30 (2 + 4 + 6 + 8 + 10)

# task 9
def get_word_with_h():
    """
    Спрашивает пользователя ввести слово с буквой 'H' или  'h'
    """
    entered_word = ""
    while "h" not in entered_word and "H" not in entered_word:
        entered_word = input("Введите слово с буквой 'H' или 'h': ")

    return entered_word

# Применение - ТУТ НЕОБХОДИМ ВВОД:
word = get_word_with_h()
print(f"Вы ввели: {word}")

# task 10 - проверяем что в строке количество символов больше либо меньше 10
def check_unique_characters(checked_string):
    uniq_chars = set(checked_string)
    if len(uniq_chars) > 10:
        return True
    else:
        return False

# Примеры
string_long = "abcdefghijklm"  # 13 символов
string_short = "aabbccddeeffg"  # 7 символов

print(f"'{string_long}': {check_unique_characters(string_long)}")  # должно быть True
print(f"'{string_short}': {check_unique_characters(string_short)}")  #должно быть False

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""