import unittest
from teachers import Teacher, DisciplineTeacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("Иванов И.И.")
        self.discipline_teacher = DisciplineTeacher("Петров П.П.", "Математика")

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.name, "Иванов И.И.")
        self.assertIn(self.teacher, Teacher.teachers_list)

    def test_discipline_teacher_creation(self):
        self.assertEqual(self.discipline_teacher.name, "Петров П.П.")
        self.assertEqual(self.discipline_teacher.discipline, "Математика")
        self.assertIn(self.discipline_teacher, Teacher.teachers_list)

    def test_fire_teacher(self):
        Teacher.fire_teacher(self.teacher)
        self.assertNotIn(self.teacher, Teacher.teachers_list)

    def test_fire_teacher_not_found(self):
        Teacher.fire_teacher(self.teacher)
        Teacher.fire_teacher(self.teacher)
        self.assertNotIn(self.teacher, Teacher.teachers_list)

if __name__ == '__main__':
    unittest.main()