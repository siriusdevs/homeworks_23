"""Module that tests functionality class Course."""
from enum import IntEnum

import pytest

from hw3 import Course, Student, Teacher


class NumberEnum(IntEnum):
    """Enumeration class representing board for number."""

    thirtythree = 33
    fivethousand = 5000
    eighteen = 18
    onethousand = 1000000
    zero = 0


info_of_course = (
    ('Programming',
     [
         Student
         (
             'Anna',
             'Asti',
             NumberEnum.thirtythree,
             'K0709-22/3',
             NumberEnum.fivethousand,
         ),
     ],
        [
         Teacher
         (
             'Boris',
             'Gomzaykov',
             NumberEnum.eighteen,
             'Higher mathematics',
             NumberEnum.onethousand,
         ),
     ],
     ),
)


@pytest.mark.parametrize('title, list_students, list_teachers', info_of_course)
def test_course_info(
    title: str,
    list_students: list[Student] | tuple[Student],
    list_teachers:  list[Teacher] | tuple[Teacher],
) -> None:
    """Check parameters.

    Args:
        title (str): title of course
        list_students (list[Student] | tuple[Student]): list students of course
        list_teachers (list[Teacher] | tuple[Teacher]): list teachers of course
    """
    course = Course(title, list_students, list_teachers)
    assert course.title == title
    assert course.list_students == list_students
    assert course.list_teachers == list_teachers


@pytest.mark.xfail(raises=(TypeError, ValueError))
def test_info_invalid():
    """Check setter work."""
    with pytest.raises(TypeError):
        Course(
            NumberEnum.zero,
            [
                ['Masha', 'Bokova', 33, 'K0709-22/3', 5000],
            ],
            ['Boris', 'Gomzaykov', 18, 'Higher mathematics', 1000000],
        )
    with pytest.raises(TypeError):
        Course('History', (
            ('Anna', 'Asti', 33, 'K0709-22/2', 4500),
            ('Mari', 'Kraimbrery', 31, 'K0709-22/1', 5000),
        ),
            ['Boris', 'Gomzaykov', 18, 'Higher mathematics', 1000000],
        )
    with pytest.raises(TypeError):
        Course('English', [
            ['Anna', 'Asti', 33, 'K0709-22/3', 4500],
            ['Mari', 'Kraimbrery', 31, 'K0709-22/1', 5000],
        ],
            ('ALbert', 'Tenigin', 18, 'OP', 1000000),
        )
    with pytest.raises(ValueError):
        course = Course('Programming', [], [])
        course.conduct_a_class()
