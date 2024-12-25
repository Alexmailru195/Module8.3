import pytest
from teachers import Teacher, DisciplineTeacher

@pytest.fixture
def teacher():
    return Teacher("Иванов И.И.")

@pytest.fixture
def discipline_teacher():
    return DisciplineTeacher("Петров П.П.", "Математика")

def test_teacher_creation(teacher):
    assert teacher.name == "Иванов И.И."
    assert teacher in Teacher.teachers_list

def test_discipline_teacher_creation(discipline_teacher):
    assert discipline_teacher.name == "Петров П.П."
    assert discipline_teacher.discipline == "Математика"
    assert discipline_teacher in Teacher.teachers_list

def test_fire_teacher(teacher):
    Teacher.fire_teacher(teacher)
    assert teacher not in Teacher.teachers_list

def test_fire_teacher_not_found(teacher):
    Teacher.fire_teacher(teacher)
    Teacher.fire_teacher(teacher)
    assert teacher not in Teacher.teachers_list