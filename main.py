class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade_l):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade_l]
            else:
                lecturer.grades_l[course] = [grade_l]
        else:
            return 'Ошибка'

    def average_rating_s(self):
        count = 0
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            for rates_s in self.grades.values():
                for rate_s in rates_s:
                    count += rate_s
                    average_rate_s = count / len(rates_s)
                return average_rate_s

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_rating_s()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_l = {}

    def average_rating_l(self):
        count = 0
        if len(self.grades_l.values()) == 0:
            return 'Ошибка'
        else:
            for rates_l in self.grades_l.values():
                for rate_l in rates_l:
                    count += rate_l
                    average_rate_l = count / len(rates_l)
                return average_rate_l

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating_l()}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res




student_1 = Student('Bill', 'Tobin', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Designer']
student_1.finished_courses += ['Tester']

student_2 = Student('Panther', 'Black', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Designer']
student_2.finished_courses += ['Java']

student_3 = Student('Tyler', 'Creator', 'male')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Git']
student_3.finished_courses += ['Tester']
student_3.finished_courses += ['Java']

lecturer_1 = Lecturer('Tommy', 'Rock')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Kim', 'Wong')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Designer']

reviewer_1 = Reviewer('Steve', 'Rogers')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Tester']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('David', 'Smith')
reviewer_2.courses_attached += ['Designer']
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 9)


print(student_1)
print()
print(student_2)
print()
print(student_3)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)








