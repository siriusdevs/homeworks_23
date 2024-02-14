"""Test module for hw3."""

import pytest

from hw3 import Enemy, Game, Player, Weapon

DAMAGE = 25
HEALTH = 100
LEVEL = 5

NEGATIVE_DMG = -25
NEGATIVE_HP = -100
NEGATIVE_LVL = -5

TEST_WEAPON = (
    ('Sword', DAMAGE),
    ('Spear', DAMAGE),
)

TEST_ERROR_WEAPON = (
    ('', DAMAGE),
    ('Void', NEGATIVE_DMG),
)

TEST_PLAYER = (
    ('Warrior', HEALTH, Weapon('Sword', DAMAGE), LEVEL),
    ('Wizard', HEALTH, Weapon('Magic Staff', DAMAGE), LEVEL),
    ('Archer', HEALTH, Weapon('Bow', DAMAGE), LEVEL),
)

TEST_ERROR_PLAYER = (
    ('Matuhin', NEGATIVE_HP, Weapon('Banana', DAMAGE), LEVEL),
    ('', HEALTH, Weapon('Coffee', DAMAGE), LEVEL),
    ('Lorena', HEALTH, Weapon('Mandarin', DAMAGE), NEGATIVE_LVL),
)

TEST_ENEMY = (
    ('Troll', HEALTH, Weapon('Keyboard', DAMAGE)),
    ('Goblin', HEALTH, Weapon('PC mouse', DAMAGE)),
    ('Quack Doctor', HEALTH, Weapon('Boot', DAMAGE)),
)

TEST_ERROR_ENEMY = (
    ('Gamer', HEALTH, LEVEL),
    ('Zadrot', DAMAGE, LEVEL),
)


@pytest.mark.parametrize('name, damage', TEST_WEAPON)
def test_weapon(name: str, damage: int | float) -> None:
    """
    Test the created objects of type weapon.

    Args:
        name (str): Weapon name.
        damage (int | float): Weapon damage.
    """
    assert Weapon(name, damage)


@pytest.mark.parametrize('name, damage', TEST_ERROR_WEAPON)
def test_error_weapon(name: str, damage: int | float) -> None:
    """
    Test the wrong created objects of type weapon.

    Args:
        name (str): Weapon name.
        damage (int | float): Weapon damage.
    """
    with pytest.raises(ValueError):
        assert Weapon(name, damage)


@pytest.mark.parametrize('name, health, weapon, level', TEST_PLAYER)
def test_player(name: str, health: int | float, weapon: Weapon, level: int) -> None:
    """
    Test the created objects of type player.

    Args:
        name (str): Player name.
        health (int | float): Player health.
        weapon (Weapon): Player weapon.
        level (int): Player level.
    """
    assert Player(name, health, weapon, level)


@pytest.mark.parametrize('name, health, weapon, level', TEST_ERROR_PLAYER)
def test_error_player(name: str, health: int | float, weapon: Weapon, level: int) -> None:
    """
    Test the wrong created objects of type player.

    Args:
        name (str): Player name.
        health (int | float): Player health.
        weapon (Weapon): Player weapon.
        level (int): Player level.
    """
    with pytest.raises(ValueError):
        assert Player(name, health, weapon, level)


@pytest.mark.parametrize('name, health, weapon', TEST_ENEMY)
def test_enemy(name: str, health: int | float, weapon: Weapon) -> None:
    """
    Test the created objects of type enemy.

    Args:
        name (str): Enemy name.
        health (int | float): Enemy health.
        weapon (Weapon): Enemy weapon.
    """
    assert Enemy(name, health, weapon)


@pytest.mark.parametrize('name, health, weapon', TEST_ERROR_ENEMY)
def test_error_enemy(name: str, health: int | float, weapon: Weapon) -> None:
    """
    Test the wrong created objects of type enemy.

    Args:
        name (str): Enemy name.
        health (int | float): Enemy health.
        weapon (Weapon): Enemy weapon.
    """
    with pytest.raises(TypeError):
        assert Enemy(name, health, weapon)


def test_add_weapon() -> None:
    """Test for add_weapon function."""
    game = Game([], [TEST_WEAPON], [])
    new_weapon = Weapon('Halberd', DAMAGE)
    game.add_weapon(new_weapon)
    assert new_weapon in game.weapons


def test_remove_weapon() -> None:
    """Test for remove_weapon function."""
    game = Game([], [TEST_WEAPON], [])
    old_weapon = Weapon('Sabre', DAMAGE)
    game.add_weapon(old_weapon)
    game.remove_weapon(old_weapon)
    assert old_weapon not in game.weapons


def test_add_player() -> None:
    """Test for add_player function."""
    game = Game([TEST_PLAYER], [], [])
    new_player = Player('Rogue', HEALTH, Weapon('Daggers', DAMAGE), LEVEL)
    game.add_player(new_player)
    assert new_player in game.players


def test_remove_player() -> None:
    """Test for remove_player function."""
    game = Game([TEST_PLAYER], [], [])
    old_player = Player('Support', HEALTH, Weapon('Magic Book', DAMAGE), LEVEL)
    game.add_player(old_player)
    game.remove_player(old_player)
    assert old_player not in game.players


def test_add_enemy() -> None:
    """Test for add_enemy function."""
    game = Game([], [], [TEST_ENEMY])
    new_enemy = Enemy('Black Wolf', HEALTH, Weapon('Claws', DAMAGE))
    game.add_enemy(new_enemy)
    assert new_enemy in game.enemies


def test_remove_enemy() -> None:
    """Test for remove_enemy function."""
    game = Game([], [], [TEST_ENEMY])
    old_enemy = Enemy('Black Psina', HEALTH, Weapon('Lapki', DAMAGE))
    game.add_enemy(old_enemy)
    game.remove_enemy(old_enemy)
    assert old_enemy not in game.enemies
