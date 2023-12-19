"""Tests for HW1."""
import pytest

from hw1.hw1 import salaries_statistic

TEST_DATA0 = {
    'DEVS': {
        'Bob': 4000.5,
        'Robert Stryzhak': 1.0,
        'YA': 1000.0,
        'Paulo Berberi': 2000.99,
        'Progeri': 1069.0,
    },
    'DESIGN': {
        'Rob': 3000.0,
        'Bobert Stryzhak': 80.5,
        'RA': 1005.0,
        'Slavic Morrrrozov': 2600.45,
        'Duck': 1008.0,
    },
    'FRONTEN_1': {
        'Dolina Albina': 30.0,
        'Chaild-Maild': 80.0,
        'Romantic': 9785.45,
        'Ericas': 290.0,
        'Levomicolas': 8973.5,
    },
    'ANALITICS': {
        'Dob': 2000.0,
        'Dobert Stryzhak': 90.45,
        'DA': 1988.0,
        'Alex Abdelnur': 2045.5,
        'Dog': 1080.0,
    },
    'HR': {
        'Pob': 3500.0,
        'Pobert Stryzhak': 92.0,
        'PA': 1907.0,
        'Dayana': 2300.9,
        'Cat': 1098.0,
    },
}
EXPECTED_DATA0 = ([19158.95, 8897.9, 8071.49], '70.8%')

TEST_DATA1 = {
    'MARKETING_CORP': {
        'Nikolai Petrov': 6890.0,
        'Iliya Donskoi': 987.23,
        'Valya Karnaval': 1890.0,
        'Amina Tamina': 3400.34,
        'Tanya RZHD': 79680.56,
    },
    'HR_MANAGMENT': {
        'Alya': 30.0,
        'Aleksandr': 80.0,
        'Romance': 9785.45,
        'Bober': 290.0,
        'Daniel': 8973.5,
    },
    'FRONTEND_2': {
        'Dolina': 30.0,
        'Chaild': 80.0,
        'Roman': 9785.45,
        'Eric': 290.0,
        'Leo': 8973.5,
    },
    'SECURITY': {
        'Dariya': 1.0,
        'Ariella': 9340.6,
        'Max': 8970.95,
        'Oleg': 5000.0,
        'Anton': 3456.0,
    },
    'CALL_CENTER': {
        'Paulo': 2132.0,
        'Kristina': 2120.87,
        'Rex': 7981.95,
        'Marina': 234.5,
        'Cat': 8912.0,
    },
}
EXPECTED_DATA1 = ([92848.13, 26768.55, 21381.32], '78.63%')

TEST_DATA2 = {
    'CONTROL_CENTER': {
        'Nikita': 6890.0,
        'Yan': 987.23,
        'Vadim Nikiforov': 1890.0,
        'Aleksandr': 3400.34,
        'Timur': 79680.56,
    },
    'MARKETING_OTDEL': {
        'Nikolai': 4500.0,
        'Iliya': 3500.0,
        'Valya': 2500.0,
        'Amina': 5500.0,
        'Tanya': 6500.0,
    },
    'SIS_ADMINS': {
        'Yamado': 3000.0,
        'Sacuki': 4000.0,
        'Kinoshito': 5000.0,
        'Hoshino': 6000.0,
        'Sakura': 7000.0,
    },
    'PLUMBER': {
        'Diana': 1500.0,
        'Tatiyana': 2500.0,
        'Elisei': 3500.0,
        'Moisei': 4500.0,
        'Shtolic': 5500.0,
    },
    'FRONTEND_3': {
        'Dolina1': 6500.0,
        'Chaild1': 7500.0,
        'Roman1': 8500.0,
        'Eric1': 9500.0,
        'Leo1': 10500.0,
    },
    'MED_CENTER': {
        'Pavel': 8000.0,
        'Kollisto': 9000.0,
        'Penelopa': 10000.0,
        'Sirena': 11000.0,
        'Iness': 12000.0,
    },
}
EXPECTED_DATA2 = ([92848.13, 50000.0, 42500.0], '74.04%')

TEST_DATA3 = {
    'ARCHIVE_OTDEL': {
        'Rubiya': 7820.0,
        'Aurora Galicina': 1007.0,
        'Liticiya Mangovna': 9810.0,
        'Ditrian Aksilim': 4500.0,
        'Edvard Kallin1': 79680.5,
    },
    'HUMOR_CENTER': {
        'Zahar Starcev': 1070.0,
        'Jakob': 8750.0,
        'Ellise': 5340.5,
        'Bred Pit': 9000.0,
        'Charli': 3500.5,
    },
    'MENEGERS': {
        'Karlael': 1000.0,
        'Bella': 4000.5,
        'Dzhasper': 3000.5,
        'Anna': 2300.0,
        'Victoriya': 6000.0,
    },
    'VET_DOCTORS': {
        'Vladlen': 3400.0,
        'Mariya': 7020.5,
        'Ognislav': 3409.95,
        'Erimei': 2304.5,
        'Prahlada': 2098.0,
    },
}
EXPECTED_DATA3 = ([101810.5, 26591.0, 13830.45], '91.62%')
LIMIT = 3000.0

TEST_DATA4 = {
    'GOS_USLUGI': {
        'Viagra': 6000.0,
        'Putya': 4987.0,
        'Lina': 9800.0,
        'Luna': 7000.5,
        'Donara': 3900.5,
    },
    'FRONTEND_4': {
        'Dolina2': 5030.0,
        'Chaild2': 1980.0,
        'Roman2': 3495.45,
        'Eric2': 8190.0,
        'Leo2': 2083.5,
    },
    'SONBE_TEACHER': {
        'Velor': 1230.0,
        'Boris': 9830.5,
        'Igor': 2931.5,
        'Anastasiya': 4829.0,
        'Alina': 9356.0,
    },
    'MED_CENTER': {
        'Katalina': 3409.0,
        'Karlo': 2390.5,
        'Ron': 3094.95,
        'Griko': 2997.5,
        'Terron': 1342.0,
    },
    'MARKETING': {
        'Nikolai': 9843.0,
        'Iliya': 4003.0,
        'Valya': 3080.0,
        'Amina': 2000.45,
        'Tanya': 6801.05,
    },
}
EXPECTED_DATA4 = ([31688.0, 24015.5, 20647.05], '85.24%')
LIMIT1 = 3809.0

TEST_DATA5 = {
    'DEPARTAMENT': {
        'Nika': 3000.0,
        'Victoriya': 3800.0,
        'Yasya': 9800.0,
        'Pasha': 5630.45,
        'Egor Litvinov': 4090.5,
    },
    'ANALITICS': {
        'Vera': 7830.0,
        'Nadezhda': 2340.0,
        'Lubov': 5982.45,
        'Boris': 8920.0,
        'Dariya': 2390.5,
    },
    'BUSINES': {
        'Daniel': 4000.0,
        'Arina': 3040.0,
        'Misha': 1090.5,
        'Egor': 3000.0,
        'Urii': 600009.0,
    },
    'CORPORATIVE_MENEGERS': {
        'Kira': 2145432.0,
        'Irina': 212322320.45,
        'Raisa': 79823232321.5,
        'Mars': 2382939824.5,
        'Sabina': 109823.0,
    },
    'MARKETING': {
        'Nikolai Zagor': 6890.0,
        'Iliya Poopov': 9087.23,
        'Valya Mirnaya': 1890.0,
        'Amina Pivnaya': 3400.34,
        'Tanya Pivnaya': 79680.56,
    },
    'MENEGERS': {
        'Karlael': 1.0,
        'Bella': 9340.6,
        'Dzhasper': 8970.95,
        'Anna': 5000.0,
        'Victoriya': 3456.0,
    },
}
EXPECTED_DATA5 = ([82420749721.45, 600009.0, 79680.56], '100.0%')
LIMIT2 = 10000.0

# НЕПРАВИЛЬНЫЕ ТЕСТЫ
W_TEST_DATA0 = [
    [
        'ARCHIVE',
        {
            'Rubi': 7820.0,
            'Aurora': 1007.0,
            'Liticiya': 9810.0,
            'Ditrian': 4500.0,
            'Edvard Kallin': 79680.5,
        },
    ],
]

W_TEST_DATA1 = {
    'ARCHIVE': [
        {
            'Rubi': 7820.0,
            'Aurora': 1007.0,
            'Liticiya': 9810.0,
            'Ditrian': 4500.0,
            'Edvard Kallin': 79680.5,
        },
    ],
    'HUMOR_CENTER_CORP': {
        'Zahar Starcev': 1070.0,
        'Jakob': 8750.0,
        'Ellise': 5340.5,
        'Bred Pit': 9000.0,
        'Charli': 3500.5,
    },
    'MENEGERS_OTDEL': [
        {
            'Karlaelw': 1000.0,
            'Bellaw': 4000.5,
            'Dzhasperw': 3000.5,
            'Annaw': 2300.0,
            'Victoriyaw': 6000.0,
        },
    ],
    'VET_DOCTORS_CORP': {
        'Vladlen': 3400.0,
        'Mariya': 7020.5,
        'Ognislav': 3409.95,
        'Erimei': 2304.5,
        'Prahlada': 2098.0,
    },
}

W_TEST_DATA2 = {
    'ARCHIVE': {
        'Rubi': 7820.0,
        'Aurora': 1007.0,
        'Liticiya': 9810.0,
        'Ditrian': 4500.0,
        'Edvard Kallin': 79680.5,
    },
    2: {
        'Zahar Starcev': 1070.0,
        'Jakob': 8750.0,
        'Ellise': 5340.5,
        'Bred Pit': 9000.0,
        'Charli': 3500.5,
    },
    'MENEGERS1': {
        'Karlaelq': 1000.0,
        'Bellaq': 4000.5,
        'Dzhasperq': 3000.5,
        'Annaq': 2300.0,
        'Victoriyaq': 6000.0,
    },
    'VET_DOCTORS1': {
        'Vladlen5': 3400.0,
        'Mariya5': 7020.5,
        'Ognislav5': 3409.95,
        'Erimei5': 2304.5,
        'Prahlada5': 2098.0,
    },
}

W_TEST_DATA3 = {
    'ARCHIVED': {
        'Rubi4': 7820.0,
        'Aurora4': 1007,
        'Liticiya4': 9810.0,
        'Ditrian4': 4500.0,
        'Edvard Kallin4': 79680.5,
    },
    2: {
        'Zahar Starcev2': 1070.0,
        'Jakob2': 8750.0,
        'Ellise2': 5340.5,
        'Bred Pit2': 9000.0,
        'Charli2': 3500.5,
    },
    'MENEGERS2': {
        'Karlael Singo': 1000.0,
        'Bella Dingo': 4000.5,
        'Dzhasper Tingo': 3000,
        'Anna Pinko': 2300.0,
        'Victoriya Linko': 6000.0,
    },
    'VET_DOCTORS2': {
        'Vladlen0': 3400.0,
        'Mariya0': 7020.5,
        'Ognislav0': 3409.95,
        'Erimei0': 2304.5,
        'Prahlada0': 2098.0,
    },
}

W_TEST_DATA4 = {
    'ARCHIVE_CORPORATION': {1: 7820.0, 2: 1007.0, 3: 9810.0, 4: 4500.0, 5: 79680.5},
    'HUMOR_CENTER': {
        'Zahar Starcev1': 1070.0,
        'Jakob1': 8750.0,
        'Ellise1': 5340.5,
        'Bred Pit1': 9000.0,
        'Charli1': 3500.5,
    },
    'MENEGERS_HUMEN': {
        'Karlael1': 1000.0,
        'Bella1': 4000.5,
        'Dzhasper1': 3000.5,
        'Anna1': 2300.0,
        'Victoriya1': 6000.0,
    },
    'VET_DOCTORS': {
        'VladlenS': 3400.0,
        'MariyaS': 7020.5,
        'OgnislavS': 3409.95,
        'ErimeiS': 2304.5,
        'PrahladaS': 2098.0,
    },
}

W_TEST_DATA6 = {
    'MARKETING': {
        'Nikolai': 20.0,
        'Iliya': -100.0,
        'Valya': 100.0,
        'Amina': -10.0,
        'Tanya': -10.0,
    },
    'HR_MANAGMENT': {
        'Alya': 10.0,
        'Aleksandr': 20.0,
        'Roman': 30.0,
        'Bober': -70.0,
        'Daniel': 10.0,
    },
    'FRONTEND': {
        'Dolina': 10.0,
        'Chaild': 10.0,
        'Roman': 10.0,
        'Eric': 10.0,
        'Leo': -40.0,
    },
    'SECURITY': {
        'Dariya': -100.0,
        'Ariella': 10.0,
        'Max': 10.0,
        'Oleg': 40.0,
        'Anton': 40.0,
    },
    'CALL_CENTER': {
        'Paulo': 10.0,
        'Kristina': 10.0,
        'Rex': 10.0,
        'Marina': -100.0,
        'Cat': 70.0,
    },
}


all_data = (
    (TEST_DATA0, None, EXPECTED_DATA0),
    (TEST_DATA1, None, EXPECTED_DATA1),
    (TEST_DATA2, None, EXPECTED_DATA2),
    (TEST_DATA3, LIMIT, EXPECTED_DATA3),
    (TEST_DATA4, LIMIT1, EXPECTED_DATA4),
    (TEST_DATA5, LIMIT2, EXPECTED_DATA5),
)


@pytest.mark.parametrize('dprts, min_salary, expected', all_data)
def test_salaries_statistic(
    dprts: dict[str, dict[str, float]],
    min_salary: float | None,
    expected: float,
):
    """Test detective function with test_all_departments.

    Args:
        dprts: dict - list of all departments, their employees and their salaries.
        min_salary: float - the num limit above which salaries are not taken, default (None).
        expected: float - an actual expected result.

    Asserts:
        True if the function returns expected results.
    """
    assert salaries_statistic(dprts, min_salary) == expected


@pytest.mark.xfail()
def test_fail_departaments_type():
    """Negative test 0."""
    with pytest.raises(TypeError):
        salaries_statistic(W_TEST_DATA0)


@pytest.mark.xfail()
def test_fail_departament_type():
    """Negative test 1."""
    with pytest.raises(TypeError):
        salaries_statistic(W_TEST_DATA1)


@pytest.mark.xfail()
def test_fail_departament_name_type():
    """Negative test 2."""
    with pytest.raises(TypeError):
        salaries_statistic(W_TEST_DATA2)


@pytest.mark.xfail()
def test_fail_worker_name_type():
    """Negative test 3."""
    with pytest.raises(TypeError):
        salaries_statistic(W_TEST_DATA3)


@pytest.mark.xfail()
def test_fail_salary_type():
    """Negative test 4."""
    with pytest.raises(TypeError):
        salaries_statistic(W_TEST_DATA4)


@pytest.mark.xfail()
def test_fail_statistic_value():
    """Negative test 6."""
    with pytest.raises(ValueError):
        salaries_statistic(W_TEST_DATA6)
