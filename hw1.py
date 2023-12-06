"""
Напишите функцию, которая принимает любые ключевые аргументы,
но ожидает, что название аргумента будет названием отдела компании (str),
а значение для аргумента - словарем,
где имена сотрудников (str) служат в качестве ключей,
а зарплаты (float) - в качестве значений .
Функция должна возвращать статистику:
топ 3 зарплат в компании списком,
отношение суммы этого топа ко всему размеру выплат в компании, в процентах.
Функция также должна принимать опциональный аргумент,
который по умолчанию равен None.
Этот аргумент - числовой предел, ниже которого зарплаты учитывать не нужно.
Все числа в выводе функции округлять до второго знака после запятой.
Оформить файл по flake8 с учетом данного вам setup.cfg.
Написать тесты.
Проверка линтера и тесты должны работать в github workflows.
"""


def salaries_statistic(
        dprts: dict[str, dict[str, float]],
        min_salary: float | None = None,
        ) -> tuple:
    """this module is designed to work with args
    (unpack departments to count sum of sellaries in all of them,
    to sort it if we hawe limit, like min_salary ),
    to make top 3 sum of sellaries in departments,
    to count precentage of top 3 sum to total salarie sum,
    to find Type and Value errors if there are in args.


    Args:
        departaments (dict[str, dict[str, float]]):
        /Names of depatments with dicts of workers-their salaries
        min_salary (float | None, optional):
        /Minimal salarie limit to sort workers salaries in future.
        /Defaults to None.

    Raises:
        TypeError: if dict type not set
        TypeError: if float type not set
        TypeError: if str not set
        ValueError: if wrong value given

    Returns:
        _type_:
        /returns top 3 salaries in departaments,
        /precentage of top 3 sum to total salary sum
    """
    answer = []
    answer1 = []
    super_total_salary = 0
    if not isinstance(dprts, dict):
        raise TypeError('departaments type is not dict')
    for departament_name, departament in dprts.items():
        if not isinstance(departament, dict):
            raise TypeError('departament type is not dict')
        if not isinstance(departament_name, str):
            raise TypeError('departamet_name type is not str')
        total_salary = 0
        for name, salary in departament.items():
            if not isinstance(name, str):
                raise TypeError(' name type is not str')
            if not isinstance(salary, float):
                raise TypeError('salary type is not float')
            salary = round(salary, 2)
            super_total_salary += salary
            if min_salary:
                if not isinstance(min_salary, float):
                    raise TypeError('min_salary type is not float')
                if salary >= min_salary:
                    total_salary += salary
            else:
                total_salary += salary
        answer.append(total_salary)
    if super_total_salary == 0:
        raise ValueError('super_total_salary = 0, на нуль делить нельзя.')
    answer = sorted(answer, reverse=True)[0:3]
    for number in answer:
        number = round(number, 2)
        answer1.append(number)
    return answer1, f'{round((sum(answer)/super_total_salary)*100, 2)}%'
