class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades_for_lectures:
                    lecturer.grades_for_lectures[course].append(grade)
                else:
                    lecturer.grades_for_lectures[course] = [grade]
            else:
                return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            num_grades += len(grades)
        return total_grades / num_grades if num_grades > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name},\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные  курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for grades in self.grades_for_lectures.values():
            total_grades += sum(grades)
            num_grades += len(grades)
        return total_grades / num_grades if num_grades > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.1f}\n')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


def average_all_students(students, course):
    total_grades = 0
    num_grades = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            num_grades += len(student.grades[course])
    return total_grades / num_grades if num_grades > 0 else 0


def average_all_lecturers(lecturers, course):
    total_grades = 0
    num_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades_for_lectures:
            total_grades += sum(lecturer.grades_for_lectures[course])
            num_grades += len(lecturer.grades_for_lectures[course])
    return total_grades / num_grades if num_grades > 0 else 0


student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Alice', 'Smith', 'female')

lecturer1 = Lecturer('Adam', "Obama")
lecturer2 = Lecturer('Mia', "Obama")

reviewer1 = Reviewer('Ann', 'Ivanova')
reviewer2 = Reviewer('Bob', 'Doe')


lecturer1.courses_attached = ['Python', 'Math']
lecturer2.courses_attached = ['Python', 'Math']

reviewer1.courses_attached = ['Python', 'Math']
reviewer2.courses_attached = ['Python', 'Math']

student1.courses_in_progress = ['Python', 'Math']
student2.courses_in_progress = ['Python', 'Math']
student1.finished_courses = ['Biology', "Design"]
student2.finished_courses = ['Biology', "Design"]

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 8)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Math', 9)
reviewer2.rate_hw(student2, 'Math', 8)
reviewer2.rate_hw(student2, 'Python', 10)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)



