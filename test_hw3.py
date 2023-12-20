from hw3 import Teacher, Student, Course, Group, EducationalInstitution

def test_teacher_create_course():
    teacher = Teacher("Иванов")
    course = teacher.create_course("Программирование")
    assert course.course_name == "Программирование"
    assert course.teacher == teacher

def test_teacher_assign_student():
    teacher = Teacher("Зайцев")
    course = Course("ОС", teacher)
    student = Student("Петров")
    teacher.assign_student(course, student)
    assert student in course.students

def test_student_enroll():
    student = Student("Сидоров")
    course = Course("ПЦУ", Teacher("Кузнецов"))
    student.enroll(course)
    assert student in course.students

def test_student_drop_course():
    student = Student("Васнецов")
    course = Course("ОФП", Teacher("Смирнов"))
    student.enroll(course)
    student.drop_course(course)
    assert student not in course.students

def test_group_add_student():
    group = Group("К0709")
    student = Student("Попов")
    group.add_student(student)
    assert student in group.students

def test_group_remove_student():
    group = Group("К0111")
    student = Student("Петров")
    group.add_student(student)
    group.remove_student(student)
    assert student not in group.students

def test_educational_institution_add_course():
    institution = EducationalInstitution()
    course = Course("Сети", Teacher("Головин"))
    institution.add_course(course)
    assert course in institution.courses

def test_educational_institution_remove_course():
    institution = EducationalInstitution()
    course = Course("Вышмат", Teacher("Иванов"))
    institution.add_course(course)
    institution.remove_course(course)
    assert course not in institution.courses

def test_educational_institution_add_group():
    institution = EducationalInstitution()
    group = Group("К0609")
    institution.add_group(group)
    assert group in institution.groups

def test_educational_institution_remove_group():
    institution = EducationalInstitution()
    group = Group("К0409")
    institution.add_group(group)
    institution.remove_group(group)
    assert group not in institution.groups
