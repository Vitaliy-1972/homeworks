class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
        Имя: {self.name} 
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self._calculate_average_grade()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}'''

    def _calculate_average_grade(self):
        grades_list = sum(list(self.grades.values()), [])
        return round(sum(grades_list) / len(grades_list), 2)

    def __lt__(self, other):
        grades_list = sum(list(self.grades.values()), [])
        grades_list_other = sum(list(other.grades.values()), [])
        average_one = round(sum(grades_list) / len(grades_list), 2)
        average_two = round(sum(grades_list_other) / len(grades_list_other), 2)
        return average_one < average_two


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def __str__(self):
        return f'''
        Имя: {self.name} 
        Фамилия: {self.surname} 
        Средняя оценка за лекции: {self._calculate_average_grade()}'''

    def _calculate_average_grade(self):
        grades_list = sum(list(self.grades.values()), [])
        return round(sum(grades_list) / len(grades_list), 2)

    def __lt__(self, other):
        grades_list = sum(list(self.grades.values()), [])
        grades_list_other = sum(list(other.grades.values()), [])
        average_one = round(sum(grades_list) / len(grades_list), 2)
        average_two = round(sum(grades_list_other) / len(grades_list_other), 2)
        return average_one < average_two


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}'''


first_student = Student('Иван', 'Иванов', 'муж')
second_student = Student('Ирина', 'Иванова', 'жен')
first_student.courses_in_progress += ['Python', 'Git']
second_student.courses_in_progress += ['Python', 'Git']

first_lecturer = Lecturer('Сергей', 'Николаев')
second_lecturer = Lecturer('Марина', 'Викторова')
first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git', 'Python']

first_reviewer = Reviewer('Николай', 'Сергеев')
second_reviewer = Reviewer('Иван', 'Николаев')

first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Git', 9)

first_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Git', 9)

first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(second_lecturer, 'Git', 7)
first_student.rate_hw(second_lecturer, 'Python', 8)
second_student.rate_hw(first_lecturer, 'Python', 9)
second_student.rate_hw(second_lecturer, 'Git', 8)
first_student.add_courses('OOP')
second_student.add_courses('OOP')

print(first_student.__str__())
print(second_student.__str__())
print(first_reviewer.__str__())
print(second_reviewer.__str__())
print(first_lecturer.__str__())
print(second_lecturer.__str__())
print(first_student < second_student)
print(first_lecturer < second_lecturer)

def calculat_average_score_students(list_students, course):
    sum_grades = 0
    count_grades = 0
    for student in list_students:
        sum_grades += sum(student.grades[course])
        count_grades += len(student.grades[course])
    return f"Cредняя оценка за домашние задания по всем студентам {round(sum_grades / count_grades, 2)}"


def calculat_average_score_lecturers(list_lecturers, course):
    sum_grades = 0
    count_grades = 0
    for lecturer in list_lecturers:
        sum_grades += sum(lecturer.grades[course])
        count_grades += len(lecturer.grades[course])
    return f"Средняя оценка за лекции всех лекторов {round(sum_grades / count_grades, 2)}"

list_students = [first_student, second_student]
list_lecturers = [first_lecturer, second_lecturer]

print(calculat_average_score_lecturers(list_lecturers, 'Python'))
print(calculat_average_score_students(list_students, 'Python'))