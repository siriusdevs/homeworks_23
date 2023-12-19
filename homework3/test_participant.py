"""Module include tests on Participant with name and maximum number."""
import pytest
from hw3 import Participant

participants = (
    ('Albert', 0, 0),
    ('Vladislav', 1, 0),
    ('Alexey B.', 100000, 100000),
    ('Daniil', 5, 5),
    ('Mikhail', 0, 1),
)


@pytest.mark.parametrize('name, max_tsk, max_proj', participants)
def test_task_param(name: str, max_tsk: int, max_proj: int) -> None:
    """Check parameters.

    Args:
        name (str): name Participant's
        max_tsk (int): maximum task Participant's
        max_proj (int): maximum project's for Participant's
    """
    participant = Participant(name, max_tsk, max_proj)
    assert participant.name == name
    assert participant.max_tsk == max_tsk
    assert participant.max_proj == max_proj


@pytest.mark.xfail(raises=ValueError)
def test_invalid_value():
    """Check setter work."""
    with pytest.raises(ValueError):
        Participant('Daniel', -5, -10)
    with pytest.raises(ValueError):
        Participant('Dima', -1, -10)


@pytest.mark.xfail(raises=TypeError)
def test_invalid_type():
    """Check setter work."""
    with pytest.raises(TypeError):
        Participant(4, 4, 4)
    with pytest.raises(TypeError):
        Participant(4, 0, 0)
