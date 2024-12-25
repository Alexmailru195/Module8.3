class Teacher:
    teachers_list = []

    def __init__(self, name):
        self.name = name
        Teacher.teachers_list.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def fire_teacher(cls, teacher):
        if teacher in cls.teachers_list:
            cls.teachers_list.remove(teacher)
            print(f'{teacher} уволен.')
        else:
            print(f'{teacher} не найден.')


class DisciplineTeacher(Teacher):
    def __init__(self, name, discipline):
        super().__init__(name)
        self.discipline = discipline

    def __str__(self):
        return f'{self.name} (Предмет: {self.discipline})'