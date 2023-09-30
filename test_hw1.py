from hw1 import get_salaries
from typing import Tuple
import pytest


data = (
    ((('1', {'1': 200.0, '2': 300.0}),
      ('2', {'3': 300.0, '4': 400.0}),
      ('3', {'5': 100.0, '6': 600.0})),
     None,
     ([600.0, 400.0, 300.0], 68.42)),

    ((('1st', {'Smith': 5.0, 'Robbinson': 10.0}),
      ('2nd', {'White': 8.0, 'Jefferson': 6.0}),
      ('3rd', {'Bale': 4.0, 'Gosling': 6.0})),
     None,
     ([10.0, 8.0, 6.0], 61.54)),

    ((('South', {'a': 2.0, 'b': 3.0}),
      ('West', {'c': 4.0, 'd': 1.0}),
      ('East', {'e': 9.0, 'f': 3.0})),
     None,
     ([9.0, 4.0, 3.0], 72.73)),

    ((('South', {'a': 2.0, 'b': 3.0}),
      ('West', {'c': 4.0, 'd': 1.0}),
      ('East', {'e': 9.0, 'f': 3.0})),
     ('South',),
     ([9.0, 4.0, 3.0], 94.12)),

    ((('1st', {'Smith': 5.0, 'Robbinson': 10.0}),
      ('2nd', {'White': 8.0, 'Jefferson': 6.0}),
      ('3rd', {'Bale': 7.0, 'Gosling': 15.0}),
      ('4th', {'Kant': 4.0, 'Dude': 11.0}),
      ('5th', {'Black': 1.0, 'Malek': 3.0})),
     ('3rd', '4th'),
     ([10.0, 8.0, 6.0], 72.73)),
)


@pytest.mark.parametrize('source, dep_except, expected', data)
def test_get_salaries(source: Tuple[tuple], dep_except: Tuple[str], expected: Tuple[list, float]):
    assert get_salaries(*source, dep_except=dep_except) == expected
