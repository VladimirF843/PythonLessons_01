class Employee:
    """Базовый класс для всех сотрудников (name, salary)."""

    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    """Класс для руководителей (department)."""

    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    """Класс для разработчиков (programming_language)."""

    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    """
    Класс TeamLead. Наследует атрибуты от Manager и Developer.
    Имеет свой атрибут team_size.
    """

    def __init__(self, team_size: int, **kwargs):
        self.team_size = team_size

        # Вызываем __init__ следующего класса в MRO (это Manager).
        super().__init__(**kwargs)


# Пример исполнения

# Схитрил - передал ВСЕ необходимые атрибуты:
team_lead = TeamLead(
    name="Сергей Лид",
    salary=120000.0,
    department="Data Science",
    programming_language="Python",
    team_size=8
)

print("✅ Объект TeamLead успешно создан и инициализирован.")
print("--- Проверка атрибутов ---")
print(f"Имя (от Employee): {team_lead.name}")
print(f"Зарплата (от Employee): {team_lead.salary}")
print(f"Отдел (от Manager): {team_lead.department}")
print(f"Язык (от Developer): {team_lead.programming_language}")
print(f"Размер команды (уникальный): {team_lead.team_size}")