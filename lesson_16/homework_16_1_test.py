import unittest


# --- Структура классов ---

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    def __init__(self, team_size: int, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)


# --- Класс для тестирования ---

class TestTeamLeadAttrs(unittest.TestCase):

    def setUp(self):
        self.lead = TeamLead(
            name="Ирина",
            salary=150000.0,
            department="QA",
            programming_language="Python",
            team_size=5
        )

    def test_all_attributes_exist(self):
        # От Employee
        self.assertTrue(hasattr(self.lead, 'name'))
        self.assertTrue(hasattr(self.lead, 'salary'))

        # От Manager
        self.assertTrue(hasattr(self.lead, 'department'))

        # От Developer
        self.assertTrue(hasattr(self.lead, 'programming_language'))

        # От TeamLead
        self.assertTrue(hasattr(self.lead, 'team_size'))


# --- Запуск тестов ---

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)