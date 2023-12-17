"""Test for hw3."""


import pytest

from hw3 import Enemy, Game, Player, Weapon

DAMAGE = 60
HEALTH_PLAYER = 35
HEALTH_ENEMY = 40
LEVEL = 5

TEST_WEAPON = (
    ('Sword', DAMAGE),
    ('Brute', DAMAGE),
)


@pytest.mark.parametrize('name_weapon, damage', TEST_WEAPON)
def test_weapon(name_weapon: str, damage: int | float) -> None:
    """
    Test funcion for weapon.

    Args:
        name_weapon (str): name of weapon.
        damage (int | float): damage of weapon.
    """
    assert Weapon(name_weapon, damage)


TEST_WEAPON_FAIL = (
    (HEALTH_PLAYER, DAMAGE),
    (True, 'chicken'),
)


@pytest.mark.parametrize('name_weapon, damage', TEST_WEAPON_FAIL)
def test_weapon_fail(name_weapon: str, damage: int | float) -> None:
    """
    Test function for wrong weapon.

    Args:
        name_weapon (str): name of weapon.
        damage (int | float): damage of weapon.
    """
    with pytest.raises(TypeError):
        assert Weapon(name_weapon, damage)


TEST_PLAYER = (
    ('Goblin', HEALTH_PLAYER, 'Stone', LEVEL),
    ('Wizard', HEALTH_PLAYER, 'Magic wang', LEVEL),
)


@pytest.mark.parametrize('name, health, weapon, level', TEST_PLAYER)
def test_player(name: str, health: int | float, weapon: str, level: int) -> None:
    """
    Test function for player.

    Args:
        name (str): name of player.
        health (int | float): health of player.
        weapon (str): weapon of player.
        level (int): level of player.
    """
    assert Player(name, health, weapon, level)


TEST_PLAYER_FAIL = (
    (DAMAGE, 'Naggets', HEALTH_PLAYER, '5054'),
    ('opa', 'djd', 'dof', 'apap'),
)


@pytest.mark.parametrize('name, health, weapon, level', TEST_PLAYER_FAIL)
def test_player_fail(name: str, health: int | float, weapon: str, level: int) -> None:
    """
    Test function for wrong player.

    Args:
        name (str): name of player.
        health (int | float): health of player.
        weapon (str): weapon of player.
        level (int): level of player.
    """
    with pytest.raises(TypeError):
        assert Weapon(name, health, weapon, level)


TEST_ENEMY = (
    ('Dragon', HEALTH_ENEMY, 'Teeth'),
    ('Druid', HEALTH_ENEMY, 'Magic'),
)


@pytest.mark.parametrize('name, health, weapon', TEST_ENEMY)
def test_enemy(name: str, health: int | float, weapon: str) -> None:
    """
    Test function for enemy.

    Args:
        name (str): name of enemy.
        health (int | float): health of enemy.
        weapon (str): weapon of enemy.
    """
    assert Enemy(name, health, weapon)


TEST_ENEMY_FAIL = (
    (HEALTH_ENEMY, DAMAGE, 'ops'),
    (HEALTH_PLAYER, 'eiei', DAMAGE),
)


@pytest.mark.parametrize('name, health, weapon', TEST_ENEMY_FAIL)
def test_enemy_fail(name: str, health: int | float, weapon: str) -> None:
    """
    Test function for wrong enemy.

    Args:
        name (str): name of enemy.
        health (int | float): health of enemy.
        weapon (str): weapon of enemy
    """
    with pytest.raises(TypeError):
        assert Enemy(name, health, weapon)


TEST_ADD_PLAYER = (
    [
        Player('Monkey', HEALTH_PLAYER, 'Stick', LEVEL),
        Player('Rabbit', HEALTH_PLAYER, 'Stone', LEVEL),
    ],
    [Weapon('Stick', DAMAGE), Weapon('Wifi', DAMAGE)],
    [Enemy('Wolf', HEALTH_ENEMY, 'Teeth'), Enemy('Tiger', HEALTH_ENEMY, 'Claws')],
)


def test_add_player():
    """
    Test function for add_player.

    Asserts:
        True if new_player add.
    """
    game = Game(*TEST_ADD_PLAYER)
    new_player = Player('Dog', HEALTH_PLAYER, 'Brain', LEVEL)
    game += new_player
    assert new_player in game.players


TEST_REMOVE_PLAYER = (
    [
        Player('Goblin', HEALTH_PLAYER, 'Lopata', LEVEL),
        Player('Wizard', HEALTH_PLAYER, 'Magic wang', LEVEL),
    ],
    [Weapon('Sword', DAMAGE), Weapon('Brute', DAMAGE)],
    [Enemy('Dragon', HEALTH_ENEMY, 'Teeth'), Enemy('Druid', HEALTH_ENEMY, 'Magic')],
)


def test_remove_player():
    """
    Test function for remove_player.

    Asserts:
        True if old_player remove.
    """
    game = Game(*TEST_REMOVE_PLAYER)
    old_player = Player('Goblin', HEALTH_PLAYER, 'Lopata', LEVEL)
    game -= old_player
    assert old_player not in game.players


TEST_ADD_WEAPON = (
    [
        Player('Pug', HEALTH_PLAYER, 'Socket', LEVEL),
        Player('Corgi', HEALTH_PLAYER, 'Bread', LEVEL),
    ],
    [Weapon('Knife', DAMAGE), Weapon('Fork', DAMAGE)],
    [Enemy('Chiheahua', HEALTH_ENEMY, 'Scream'), Enemy('Doberman', HEALTH_ENEMY, 'Evil face')],
)


def test_add_weapon():
    """
    Test function for add_weapon.

    Asserts:
        True if new_weapon add.
    """
    game = Game(*TEST_ADD_WEAPON)
    new_weapon = Weapon('Pillow', 10)
    game += new_weapon
    assert new_weapon in game.weapons


TEST_REMOVE_WEAPON = (
    [
        Player('Pug', HEALTH_PLAYER, 'Socket', LEVEL),
        Player('Corgi', HEALTH_PLAYER, 'Bread', LEVEL),
    ],
    [Weapon('Pan', DAMAGE), Weapon('Plate', DAMAGE)],
    [Enemy('Chiheahua', HEALTH_ENEMY, 'Scream'), Enemy('Doberman', HEALTH_ENEMY, 'Evil face')],
)


def test_remove_weapon():
    """
    Test function for remove_weapon.

    Asserts:
        True if old_weapon remove.
    """
    game = Game(*TEST_REMOVE_WEAPON)
    old_weapon = Weapon('Pan', DAMAGE)
    game -= old_weapon
    assert old_weapon not in game.weapons


TEST_ADD_ENEMY = (
    [
        Player('Fedya', HEALTH_PLAYER, 'Katana', LEVEL),
        Player('Matvey', HEALTH_PLAYER, 'Laptop', LEVEL),
    ],
    [Weapon('Bottle', DAMAGE), Weapon('Laptop', DAMAGE)],
    [Enemy('Schreck', HEALTH_ENEMY, 'Power'), Enemy('Skibidy', HEALTH_ENEMY, 'Song')],
)


def test_add_enemy():
    """
    Test function for add_enemy.

    Asserts:
        True if new_enemy add.
    """
    game = Game(*TEST_ADD_ENEMY)
    new_enemy = Enemy('Black man', HEALTH_ENEMY, 'Black magic')
    game += new_enemy
    assert new_enemy in game.enemies


TEST_REMOVE_ENEMY = (
    [
        Player('Fedya', HEALTH_PLAYER, 'Katana', LEVEL),
        Player('Matvey', HEALTH_PLAYER, 'Laptop', LEVEL),
    ],
    [Weapon('Potato', DAMAGE), Weapon('Cucumber', DAMAGE)],
    [Enemy('Skibidy', HEALTH_ENEMY, 'Song'), Enemy('Schreck', HEALTH_ENEMY, 'Power')],
)


def test_remove_enemy():
    """
    Test function for remove_enemy.

    Asserts:
        True if old_enemy remove.
    """
    game = Game(*TEST_REMOVE_ENEMY)
    old_enemy = Enemy('Schreck', HEALTH_ENEMY, 'Power')
    game -= old_enemy
    assert old_enemy not in game.enemies
