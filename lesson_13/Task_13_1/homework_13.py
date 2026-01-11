"""
Візьміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""

import csv


class Compare_Union:
    """
    СОздаем класс для сравнения и обьединения исходных файлов
    """

    def __init__(self, inputs, output):
        # Файли для читання
        self.inputs = inputs
        # Файл для запису результату
        self.output = output
        # Список, куди ми зберемо всі рядки
        self.all_data = []

    def load(self):
        """
        считываем данные и заносим в список all_data.
        """
        for name in self.inputs:
            # Використовуємо оператор += для швидкого додавання списку до списку
            with open(name, newline='') as f:
                self.all_data += list(csv.reader(f))

    def dedupe(self):
        """
       убираем дубликаты
        """
        unique_list = []
        for row in self.all_data:

            if row not in unique_list:
                unique_list.append(row)

        self.all_data = unique_list

    def save(self):

        if not self.all_data:
            print("Немає даних для збереження!")
            return

        with open(self.output, 'w', newline='') as f:
            # writerows() записує одразу всі рядки зі списку
            csv.writer(f).writerows(self.all_data)
        print(f"Дані збережено у {self.output}")

#Исходные файлы
files = ['random.csv', 'r-m-c.csv']
#результат в файл
result = 'result_no_dubl_file.csv'

# Инстанс класса
union = Compare_Union(files, result)

#Выполнение
union.load()
union.dedupe()
union.save()