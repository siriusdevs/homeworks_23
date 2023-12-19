"""Module include tests on Team with Participant and maximum numbers."""
import pytest
from hw3 import Participant, Team

participant = [
    Participant('Mikhail', 4, 0),
    Participant('Anastasiya', 2, 2),
    Participant('Vyacheslav', 0, 0),
    Participant('Alexey B.', 100, 10),
]

teams = (
    ('Masters team', [participant[0], participant[3]]),
    ('College team', [participant[1:2]]),
    ('Sirius team', [participant]),
)

my_team = (Team('Dream Team', [Participant('Mikhail', 10, 10)]))

my_startup = (
    (
        Team('FEDYASYS', [Participant('Alexey', 6, 9), Participant('Anastasiya', 3, 1)]),
        "Members FEDYASYS: ['Alexey', 'Anastasiya']",
    ),
    (
        Team('College Team', [Participant('Albert', 1, 0), Participant(
            'Vyacheslav', 0, 1,
            ),
        ]),
        "Members College Team: ['Albert', 'Vyacheslav']",
    ),
)


@pytest.mark.parametrize('title, members', teams)
def test_task_param(title: str, members: list[Participant]) -> None:
    """Check parameters.

    Args:
        title (str): name of project
        members (list[Participant]): team members
    """
    team = Team(title, members)
    assert team.title == title and team.members == members


@pytest.mark.parametrize('member', participant)
def test_append(member: Participant) -> None:
    """Function which test add Member and remove Member.

    Args:
        member (Participant): task object type Participant
    """
    my_team.add_member(member)
    assert my_team.members[-1] == member

    my_team.remove_member(member)
    assert member not in my_team.members


@pytest.mark.parametrize('teams, expected', my_startup)
def test_filtered(team: Team, expected: str) -> None:
    """Function which checking work __str__.

    Args:
        team (Team): object type Team
        expected (str): expected result
    """
    assert team.__str__() == expected
