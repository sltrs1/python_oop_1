"""
Этот файл содержит решение 2-й задачи 1-го домашнего задания по теме ООП

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

    def rate_lecture(self, lecturer, course, grade):
        """Оценить работу лектора.

        Аргументы:
            lecturer (Lecturer): Объект лектора, которому выставляется оценка.
            course (str): Название курса, по которому оценивается работа.
            grade (int): Оценка за курс.

        Возвращает:
            None | str: Возвращает 'Ошибка', если переданы некорректные данные, иначе - None.
        """
        if not isinstance(lecturer, Lecturer):
            return "Ошибка"  # Можно оценивать только лекторов

        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return "Ошибка"  # Курс не найден у студента или лектора

        # Добавляем оценку лектору
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]

        return None  # Прописано явное возвращение, чтобы IDE не выдавала ворнингов


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


class Lecturer(Mentor):
    """Класс, представляющий лектора.

    Наследуется от:
        Mentor

    Атрибуты:
        name (str): Имя лектора.
        surname (str): Фамилия лектора.
        courses_attached (list): Список курсов, которые лектор ведёт.
        grades (dict): Оценки от студентов студента по курсам.
                       Ключ — название курса, значение — список оценок (list[int]).
    """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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

    def rate_hw(self, student, course, grade):
        """Оценить домашнюю работу студента.

        Аргументы:
            student (Student): Объект студента, которому выставляется оценка.
            course (str): Название курса, по которому оценивается работа.
            grade (int): Оценка за домашнее задание.

        Возвращает:
            None | str: Возвращает 'Ошибка', если переданы некорректные данные, иначе - None.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def main():
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Алёхина', 'Ольга', 'Ж')

    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']

    print(student.rate_lecture(lecturer, 'Python', 7))  # None
    print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
    print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
    print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

    print(lecturer.grades)  # {'Python': [7]}


if __name__ == "__main__":
    main()
