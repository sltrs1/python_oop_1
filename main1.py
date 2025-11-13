"""
Этот файл содержит решение 1-й задачи 1-го домашнего задания по теме ООП

Автор: Sergei Uzhva
Дата: 13.11.2025
"""


class Student:
    """Класс, представляющий студента.

    Атрибуты:
        name (str): Имя студента.
        surname (str): Фамилия студента.
        gender (str): Пол студента.
        finished_courses (list): Список завершённых курсов.
        courses_in_progress (list): Список текущих курсов, которые студент проходит.
        grades (dict): Оценки студента по курсам.
                       Ключ — название курса, значение — список оценок (list[int]).
    """

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    """Базовый класс, представляющий наставника (преподавателя или проверяющего).

    Атрибуты:
        name (str): Имя наставника.
        surname (str): Фамилия наставника.
        courses_attached (list): Список курсов, к которым наставник прикреплён.
    """

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """Оценить домашнюю работу студента.

        Аргументы:
            student (Student): Объект студента, которому выставляется оценка.
            course (str): Название курса, по которому оценивается работа.
            grade (int): Оценка за домашнее задание.

        Возвращает:
            None | str: Возвращает 'Ошибка', если переданы некорректные данные.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    """Класс, представляющий лектора.

    Наследуется от:
        Mentor

    Атрибуты:
        name (str): Имя лектора.
        surname (str): Фамилия лектора.
        courses_attached (list): Список курсов, которые лектор ведёт.
    """

    def __init__(self, name, surname):
        super().__init__(name, surname)


class Reviewer(Mentor):
    """Класс, представляющий проверяющего (ревьюера).

    Наследуется от:
        Mentor

    Атрибуты:
        name (str): Имя проверяющего.
        surname (str): Фамилия проверяющего.
        courses_attached (list): Список курсов, по которым проверяющий выставляет оценки.
    """

    def __init__(self, name, surname):
        super().__init__(name, surname)


def main():
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    print(isinstance(lecturer, Mentor))  # True
    print(isinstance(reviewer, Mentor))  # True
    print(lecturer.courses_attached)  # []
    print(reviewer.courses_attached)  # []


if __name__ == "__main__":
    main()
