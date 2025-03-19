class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer,
                          Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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
                f' Фамилия: {self.surname}\n'
                f' Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
                f' Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f' Завершенные  курсы: {", ".join(self.finished_courses)}')

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
                f' Фамилия: {self.surname}\n'
                f' Средняя оценка за лекции: {self.average_grade():.1f}')


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
                f' Фамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)