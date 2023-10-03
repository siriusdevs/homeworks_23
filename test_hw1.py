import pytest
from hw1 import generete_report

test_cases = (
    ((('Отдел продаж', [1000, 1000, 1000]),
      ('Отдел разработки', [5000, 5000, 5000]),
      ('Отдел аналитики', [6000, 5000, 6000]),
      ('Отдел маркетинга', [0, 0])), 
      None,
    (['Отдел маркетинга', 'Отдел продаж', 'Отдел разработки'], ['Отдел аналитики', 'Отдел разработки', 'Отдел продаж'])),
    ((('Отдел аналитики', [9999, 10000, 9999])),
     None,
     (['Отдел аналитики'], ['Отдел аналитики'])),
    )

@pytest.mark.parametrize("data, exceptions, expected", test_cases) 
def test_get_report(data, exceptions, expected):
  if len(data) == 1:
    d = data[0]  
  else:
    d = data
  
  assert generete_report(d, exceptions=exceptions) == expected