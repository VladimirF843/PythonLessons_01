class Rhomb:
    """
    Класс для представления Ромба.
    Использует __setattr__ для валидации и автоматических расчетов.
    """

    def __init__(self, сторона_а: float, угол_а: float):
        self.сторона_а = сторона_а
        self.угол_а = угол_а

    def __setattr__(self, name: str, value: float):

        # Валидация стороны_а (должна быть > 0)
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Сторона должна быть больше 0.")
            super().__setattr__(name, value)
            return

        # Валидация и расчет угла_б
        if name == "угол_а":
            # Угол должен быть в диапазоне (0, 180)
            if not (0 < value < 180):
                raise ValueError("Угол должен быть в пределах от 0° до 180°.")

            super().__setattr__("угол_а", value)

            # Автоматический расчет смежного угла: угол_а + угол_б = 180°
            угол_б = 180.0 - value
            super().__setattr__("угол_б", угол_б)
            return

        # Установка прочих атрибутов
        super().__setattr__(name, value)


# --- Пример использования ---
rhomb_figure = Rhomb(15, 75)
print(f"Ромб создан: Сторона={rhomb_figure.сторона_а}, Угол А={rhomb_figure.угол_а}°, Угол Б={rhomb_figure.угол_б}°")

rhomb_figure.угол_а = 110
print(f"Угол изменен: Новый Угол А={rhomb_figure.угол_а}°, Новый Угол Б={rhomb_figure.угол_б}°")