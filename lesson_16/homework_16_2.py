from abc import ABC, abstractmethod
import math


# Абстрактный базовый класс (шаблон, задающий правила)
class Figure(ABC):

    @abstractmethod
    def area(self):
        # Должен возвращать площадь фигуры
        pass

    @abstractmethod
    def perimeter(self):
        # Должен возвращать периметр фигуры
        pass


# --- Классы фигур ---

class Square(Figure):

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона должна быть больше 0.")
        self._side = side  # Приватный атрибут для хранения длины стороны

    def area(self):
        return self._side * self._side

    def perimeter(self):
        return 4 * self._side


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0.")
        self._radius = radius  # Приватный атрибут для хранения радиуса

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self._radius


class Rectangle(Figure):

    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше 0.")
        self._length = length  # Приватный атрибут для длины
        self._width = width  # Приватный атрибут для ширины

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


# Использование

# Список объектов
figures = [
    Square(side=10),
    Circle(radius=5),
    Rectangle(length=8, width=3),
]

print("=== Расчет Площади и Периметра Фигур ===")

# Перебор фигур и вывод
for i, figure in enumerate(figures):
    # Получаем имя класса для вывода
    name = type(figure).__name__
    P = figure.perimeter()
    S = figure.area()

    print("-" * 35)
    print(f"Фигура {i + 1}: **{name}**")
    print(f"  Площадь (S): {S:.2f}")
    print(f"  Периметр (P): {P:.2f}")

print("-" * 35)