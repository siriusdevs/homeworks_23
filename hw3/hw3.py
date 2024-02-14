"""Module hw3 - A simple computer game.

Задание: Компьютерная игра
Опишите архитектуру классов для компьютерной игры. Вам нужно создать следующие классы:

Класс "Оружие":
Поля:
Название оружия
Урон оружия
Методы:
Геттеры и сеттеры для полей

Класс "Юнит":
Имя
Здоровье
Оружие
Методы:
Геттеры и сеттеры для полей
Атаковать (кого == объект класса "Юнит")

Класс "Игрок" (наследуется от "Юнит"):
Поля:
Уровень игрока
Методы:
Геттеры и сеттеры для полей

Класс "Враг" (наследуется от "Юнит")

Класс "Игра":
Поля:
Список игроков (массив или список объектов класса "Игрок")
Список оружия (массив или список объектов класса "Оружие")
Список врагов (массив или список объектов класса "Враг")
Методы:
Добавить игрока
Удалить игрока
Добавить оружие
Удалить оружие
Добавить врага
Удалить врага
"""
from typing import Any, Optional


def check(new_value: Any, classes: tuple[type] | type[Any], is_positive: Optional[bool] = False):
    """
    Check a variable, type and positive.

    Args:
        new_value (Any): The value to be check for type.
        classes (tuple[type] | type[Any]): Possible data types.
        is_positive (Optional[bool], optional): Check if value is positive. Defaults to False.

    Raises:
        TypeError: If value is of wrong type.
        ValueError: If value is negative.
    """
    if not isinstance(new_value, classes):
        if isinstance(classes, tuple):
            classnames = [class_.__name__ for class_ in classes]
        else:
            classnames = classes.__name__
        value_type = type(new_value).__name__
        message = f'The {new_value} should be of {classnames}, got type {value_type}'
        raise TypeError(message)
    if is_positive and new_value < 0:
        raise ValueError(f'Value can be positive or equal zero, not {new_value}.')


class Weapon:
    """Class of weapon."""

    def __init__(self, name: str, damage: int | float) -> None:
        """
        Initialize the name of the weapon and its damage.

        Args:
            name (str): Weapon name.
            damage (int | float): Damage of weapon.
        """
        self.name = name
        self.damage = damage

    @property
    def name(self) -> str:
        """
        Getter for name of a weapon.

        Returns:
            str: Return name of the weapon.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Setter for name of a weapon.

        Args:
            new_name (str): New weapon name.

        Raises:
            ValueError: If name is empty.
        """
        check(new_name, (str))
        if new_name == '':
            raise ValueError('Weapon must have name.')
        self._name = new_name

    @property
    def damage(self) -> int | float:
        """
        Getter for damage of the weapon.

        Returns:
            int | float: Damage of the weapon.
        """
        return self._damage

    @damage.setter
    def damage(self, new_damage: int | float) -> None:
        """
        Setter for damage of the weapon.

        Args:
            new_damage (int | float): New damage of the weapon.
        """
        check(new_damage, (int | float), is_positive=True)
        self._damage = new_damage

    def __str__(self) -> str:
        """
        Display the name and characteristics of the weapon.

        Returns:
            str: Weapon name and its damage.
        """
        return f'Weapon {self.name} with {self.damage} damage'


class Unit:
    """Class of unit."""

    def __init__(self, name: str, health: int | float, weapon: Weapon) -> None:
        """
        Initialize the name, health and weapon for the unit.

        Args:
            name (str): Unit name.
            health (int | float): Health of unit.
            weapon (Weapon): Weapon of unit.
        """
        self.name = name
        self.health = health
        self.weapon = weapon

    @property
    def name(self) -> str:
        """
        Getter for unit name.

        Returns:
            str: Name of unit.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Setter for name of the unit.

        Args:
            new_name (str): New unit name.

        Raises:
            ValueError: If name is empty.
        """
        check(new_name, (str))
        if new_name == '':
            raise ValueError('Unit must have name.')
        self._name = new_name

    @property
    def health(self) -> int | float:
        """
        Getter for health of the unit.

        Returns:
            int | float: Health of the unit.
        """
        return self._health

    @health.setter
    def health(self, new_health) -> None:
        """
        Setter for health of the unit.

        Args:
            new_health (int | float): New health of the unit.
        """
        check(new_health, (int | float), is_positive=True)
        self._health = new_health

    @property
    def weapon(self) -> Weapon:
        """
        Getter for the weapon.

        Returns:
            Weapon: The weapon with name and damage.
        """
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon: Weapon) -> None:
        """
        Setter for the weapon.

        Args:
            new_weapon (Weapon): The weapon with name and damage.
        """
        check(new_weapon, (Weapon))
        self._weapon = new_weapon

    def attack(self, other_unit: type) -> str:
        """
        Display a fight between two units.

        Args:
            other_unit (type): Other unit.

        Returns:
            str: Display an attack of unit.
        """
        check(other_unit, (Unit))
        return f'{self.name} is attacking {other_unit.name}'

    def __str__(self) -> str:
        """
        Display unit name, hp and his weapon.

        Returns:
            str: Unit characteristic
        """
        return f'{self.name} with {self.health} HP, {self.weapon}'


class Player(Unit):
    """Class of player."""

    def __init__(self, name: str, health: int | float, weapon: Weapon, level: int) -> None:
        """
        Initialize name, health, weapon and level for the player.

        Args:
            name (str): Player name.
            health (int | float): Player health.
            weapon (Weapon): Player weapon.
            level (int): Player level
        """
        super().__init__(name, health, weapon)
        self.level = level

    @property
    def level(self) -> int:
        """
        Getter for the level.

        Returns:
            int: Level of player.
        """
        return self._level

    @level.setter
    def level(self, new_level: int) -> None:
        """
        Setter for the level.

        Args:
            new_level (int): New level for the player.
        """
        check(new_level, (int), is_positive=True)
        self._level = new_level

    def __str__(self) -> str:
        """
        Display player name, health, weapon and level.

        Returns:
            str: Player characteristic.
        """
        return f'{self.name} with {self.health} HP, {self.weapon}, level {self.level}'


class Enemy(Unit):
    """Class of enemy."""


class Game:
    """Class of game."""

    def __init__(self, players: list[Player], weapons: list[Weapon], enemies: list[Enemy]) -> None:
        """
        Initialize the lists of players, weapons and enemies.

        Args:
            players (list[Player]): List with players.
            weapons (list[Weapon]): List with weapons.
            enemies (list[Enemy]): List with enemies.
        """
        self.players = players
        self.weapons = weapons
        self.enemies = enemies

    def add_player(self, new_player: Player) -> None:
        """
        Add a player to the list of players.

        Args:
            new_player (Player): The player being added.

        Raises:
            ValueError: If the player is already in the list.
        """
        if new_player in self.players:
            raise ValueError(f'Player {new_player.name} already exists')
        self.players.append(new_player)

    def remove_player(self, old_player: Player) -> None:
        """
        Remove a player from the list of players.

        Args:
            old_player (Player): The player being removed.

        Raises:
            ValueError: If the player is not in the list.
        """
        if old_player not in self.players:
            raise ValueError(f'Player {old_player.name} is not exist')
        self.players.remove(old_player)

    def add_weapon(self, new_weapon: Weapon) -> None:
        """
        Add a weapon to the list of weapons.

        Args:
            new_weapon (Weapon): The weapon being added.

        Raises:
            ValueError: If the weapon is already in the list.
        """
        if new_weapon in self.weapons:
            raise ValueError(f'Weapon {Weapon.name} already exists')
        self.weapons.append(new_weapon)

    def remove_weapon(self, old_weapon: Weapon) -> None:
        """
        Remove a weapon from the list of weapons.

        Args:
            old_weapon (Weapon): The weapon being removed.

        Raises:
            ValueError: If the weapon is not in the list.
        """
        if old_weapon not in self.weapons:
            raise ValueError(f'Weapon {old_weapon.name} is not exist')
        self.weapons.remove(old_weapon)

    def add_enemy(self, new_enemy: Enemy) -> None:
        """
        Add a enemy to the list of enemies.

        Args:
            new_enemy (Enemy): The enemy being added.

        Raises:
            ValueError: If the enemy is already in the list.
        """
        if new_enemy in self.enemies:
            raise ValueError(f'Enemy {new_enemy.name} already exists')
        self.enemies.append(new_enemy)

    def remove_enemy(self, old_enemy: Enemy) -> None:
        """
        Remove a enemy from the list of enemies.

        Args:
            old_enemy (Enemy): The enemy being removed.

        Raises:
            ValueError: If the enemy is not in the list.
        """
        if old_enemy not in self.enemies:
            raise ValueError(f'Enemy {old_enemy.name} is not exist')
        self.enemies.remove(old_enemy)
