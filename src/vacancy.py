class Vacancy:
    __slots__ = ['name', 'url', 'salary', 'description']

    def __init__(self, name: str, url: str, salary: int, description: str):
        self.name = name
        self.url = url
        self.salary = salary if salary else 0
        self.description = description

    def to_dict(self):
        """Возвращает представление объекта в виде словаря"""
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary if self.salary != 0 else 'Зарплата не указана',
            'description': self.description
        }

    def __eq__(self, other):
        """Проверка на равенство зарплат"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        """Проверка, что текущая зарплата меньше другой"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary