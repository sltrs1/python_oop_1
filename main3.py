"""
Этот файл содержит решение 3-й задачи 1-го домашнего задания по теме ООП

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

    def get_avg_grade(self):
        """Подсчитать средний балл студента

        Возвращает:
            int: Средний балл.
        """
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        return avg_grade

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

        if (course not in self.courses_in_progress and
            course not in self.finished_courses) or \
            (course not in lecturer.courses_attached):
            return "Ошибка" # Курс не найден у студента или лектора

        # Добавляем оценку лектору
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]

        return None  # Прописано явное возвращение, чтобы IDE не выдавала ворнингов

    def __str__(self):

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.get_avg_grade():.2f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        )

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()


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

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
        )


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

    def get_avg_grade(self):
        """Подсчитать средний балл преподавателя

        Возвращает:
            int: Средний балл.
        """
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        return avg_grade

    def __str__(self):

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.get_avg_grade():.2f}\n"
        )

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()

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

    def __str__(self):
        return super().__str__()


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
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Федор', 'Большаков')
    reviewer = Reviewer('Пётр', 'Петров')
    student1 = Student('Алёхина', 'Ольга', 'Ж')
    student2 = Student('Василий', 'Васильев', 'M')

    student1.courses_in_progress += ['Python', 'Java']
    student2.courses_in_progress += ['Python', 'Java']

    student1.finished_courses += ['Введение в программирование']
    student2.finished_courses += ['Введение в программирование']

    lecturer1.courses_attached += ['Python', 'C++', 'Java']
    lecturer2.courses_attached += ['Введение в программирование']
    reviewer.courses_attached += ['Python', 'C++', 'Java']

    student1.rate_lecture(lecturer1, 'Python', 7)
    student2.rate_lecture(lecturer1, 'Python', 8)

    student1.rate_lecture(lecturer2, 'Введение в программирование', 10)
    student2.rate_lecture(lecturer2, 'Введение в программирование', 9)

    reviewer.rate_hw(student1, 'Python', 10)
    reviewer.rate_hw(student1, 'Python', 9)
    reviewer.rate_hw(student2, 'Python', 8)
    reviewer.rate_hw(student2, 'Python', 7)

    reviewer.rate_hw(student1, 'Java', 6)
    reviewer.rate_hw(student2, 'Java', 5)

    print(student1)
    print(student2)
    print(lecturer1)
    print(lecturer2)
    print(reviewer)
    print('----------')
    print('Операторы сравнения для студентов')
    print(student1 == student2)
    print(student1 > student2)
    print(student1 < student2)
    print('----------')
    print('Операторы сравнения для преподавателей')
    print(lecturer1 == lecturer2)
    print(lecturer1 > lecturer2)
    print(lecturer1 < lecturer2)


if __name__ == "__main__":
    main()
