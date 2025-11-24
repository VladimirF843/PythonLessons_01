class  Student:
    def __init__(self, name, firstname, age, avg_point):
        self.name = name
        self.firstname = firstname
        self.age = age
        self.avg_point = avg_point

    def show(self):
        """Выводит информацию."""
        print(f"{self.name} {self.firstname}, {self.age} лет. Средний бал: {self.avg_point}")

    def set_new(self, new_avg_point):
        """Изменяет балл."""
        self.avg_point = new_avg_point
        print(f" Средний балл обновлен до: {new_avg_point}")



#Создаем инстанс класса
student = Student("Мария", "Лученко", 20, 3.6)

# Выводим информацию по методу
student.show()
# Виведет: Мария Лученко, 20 років. Средний балл: 3.6

# Смена среднего балла
student.set_new(4.5)
# Виведе:  Средний балл обновлен до: 4.5

# Вывод новой информации
student.show()
# Виводит: Марія Лученко, 20 років. Средний балл: 4.5