"""Module hw3."""

from typing import Any, Self


def check(new_value: Any, classes: tuple[type] | type[Any]):
    """
    Check a variable and type.

    Args:
        new_value (Any): the value that the function takes.
        classes (tuple[type] | type[Any]): possible argument types.

    Raises:
        TypeError: error if argument is of wrong type.
    """
    if not isinstance(new_value, classes):
        value_type = type(new_value).__name__
        if isinstance(classes, tuple):
            classnames = [class_.__name__ for class_ in classes]
        else:
            classnames = classes.__name__
        raise TypeError(f'{new_value} of {value_type} should be of {classnames}')


class Weapon:
    """Class for weapons."""

    def __init__(self, name_weapon: str, damage: int | float) -> None:
        """
        Name of weapon and its damage.

        Args:
            name_weapon (str): name of weapon.
            damage (float): damage of weapon.
        """
        self.name_weapon = name_weapon
        self.damage = damage

    def __str__(self) -> str:
        """
        Display the name and characteristics a weapon.

        Returns:
            str: string with name of weapon.
        """
        return self.name_weapon

    @property
    def name_weapon(self) -> str:
        """
        Getter for name of a weapon.

        Returns:
            str: name of a weapon.
        """
        return self._name_weapon

    @name_weapon.setter
    def name_weapon(self, new_name_weapon: str) -> None:
        """
        Setter for name of a weapon.

        Args:
            new_name_weapon (str): new name of a weapon.
        """
        check(new_name_weapon, (str))
        self._name_weapon = new_name_weapon

    @property
    def damage(self) -> float | int:
        """
        Getter for damage of a weapon.

        Returns:
            float | int: damage of a weapon.
        """
        return self._damage

    @damage.setter
    def damage(self, new_damage: str) -> None:
        """
        Setter for damage of a weapon.

        Args:
            new_damage (str): new damage of a weapon.

        Raises:
            ValueError: error if damage is less than zero.
        """
        check(new_damage, (float | int))
        if new_damage < 0:
            raise ValueError(f'Damage of {self.name_weapon} is less than zero')
        self._damage = new_damage


class Unit:
    """Class with units."""

    def __init__(self, name: str, health: int | float, weapon: str) -> None:
        """
        Name, health and weapon for unit.

        Args:
            name (str): name of unit.
            health (int | float): health of unit.
            weapon (str): weapon of unit.
        """
        self.name = name
        self.health = health
        self.weapon = weapon

    @property
    def name(self) -> str:
        """
        Getter for name of unit.

        Returns:
            str: string with name of unit.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Setter for name of unit.

        Args:
            new_name (str): new name of unit.
        """
        check(new_name, (str))
        self._name = new_name

    @property
    def health(self) -> int | float:
        """
        Getter for health of unit.

        Returns:
            int | float: health of unit.
        """
        return self._health

    @health.setter
    def health(self, new_health: int | float) -> None:
        """
        Setter for health of unit.

        Args:
            new_health (int | float): new health of unit.

        Raises:
            ValueError: error if health is less than zero.
        """
        check(new_health, (int | float))
        if new_health < 0:
            raise ValueError(f'Health {self.health} is less than zero')
        self._health = float(new_health) if new_health is int else new_health

    @property
    def name_weapon(self) -> str:
        """
        Getter for name of weapon.

        Returns:
            str: string with the name of weapon
        """
        return self._name_weapon

    @name_weapon.setter
    def name_weapon(self, new_name_weapon: str) -> None:
        """
        Setter for name of weapon.

        Args:
            new_name_weapon (str): string with new name of weapon.
        """
        check(new_name_weapon, (str))
        self._name_weapon = new_name_weapon

    def __str__(self) -> str:
        """
        Display the characteristics of a unit.

        Returns:
            str: string with name of a unit.
        """
        return self.name

    def attack(self, other_unit: Self) -> None:
        """
        Display a string.

        Args:
            other_unit (Self): other unit.

        Returns:
            _type_: string with attack.
        """
        return f'{self.name} is attacking {other_unit.name}'


class Player(Unit):
    """Class players."""

    def __init__(self, name: str, health: int | float, weapon: str, level: int) -> None:
        """
        Create name, health, weapon and level for player.

        Args:
            name (str): name of player.
            health (int | float): health of player.
            weapon (str): weapon of player.
            level (int): level of player.
        """
        super().__init__(name, health, weapon)
        self.level = level

    def __str__(self) -> str:
        """
        Display the characteristics of a player.

        Returns:
            str: string with name of a player.
        """
        return self.name

    @property
    def level(self) -> int:
        """
        Getter for level.

        Returns:
            int: level of player.
        """
        return self._level

    @level.setter
    def level(self, new_level: int) -> None:
        """
        Setter for level.

        Args:
            new_level (int): new level for player.

        Raises:
            ValueError: error if level less than zero.
        """
        check(new_level, (int))
        if new_level < 0:
            raise ValueError('Your level is less than zero')
        self._level = new_level


class Enemy(Unit):
    """Class enemies."""

    def __str__(self) -> str:
        """
        Display the characteristics of a enemy.

        Returns:
            str: string with name of a enemy.
        """
        return self.name


class Game:
    """Class game."""

    def __init__(self, players: list[Player], weapons: list[Weapon], enemies: list[Enemy]) -> None:
        """
        Create players, weapons and enemies.

        Args:
            players (list[Player], optional): list with players.
            weapons (list[Weapon], optional): list with weapons.
            enemies (list[Enemy], optional): list with enemies.
        """
        self.__players = players
        self.__weapons = weapons
        self.__enemies = enemies

    def __iadd__(self, new_object: Player | Weapon | Enemy) -> Self:
        """
        Add new object.

        Args:
            new_object (Player | Weapon | Enemy): object to add.

        Raises:
            TypeError: error if new object not Player|Weapon|Enemy.

        Returns:
            Self: new object.
        """
        match new_object.__class__.__name__:
            case Player.__name__:
                self._add_player(new_object)
            case Weapon.__name__:
                self._add_weapon(new_object)
            case Enemy.__name__:
                self._add_enemy(new_object)
            case _:
                new_type_object = type(new_object)
                raise TypeError(f'{new_type_object} must be Player|Weapon|Enemy')
        return self

    def __isub__(self, old_object: Player | Weapon | Enemy) -> Self:
        """
        Remove old object.

        Args:
            old_object (Player | Weapon | Enemy): object to remove.

        Raises:
            TypeError: error if new object not Player|Weapon|Enemy.

        Returns:
            Self: old object.
        """
        match old_object.__class__.__name__:
            case Player.__name__:
                self._remove_player(old_object)
            case Weapon.__name__:
                self._remove_weapon(old_object)
            case Enemy.__name__:
                self._remove_enemy(old_object)
            case _:
                old_type_object = type(old_object)
                raise TypeError(f'{old_type_object} must be Player|Weapon|Enemy')
        return self

    @property
    def players(self) -> list[Player]:
        """
        Getter for players.

        Returns:
            list[Player]: list with players.
        """
        return self.__players

    def _add_player(self, new_player: Player) -> None:
        if new_player in self.__players:
            raise ValueError('This player already exists')
        self.players.append(new_player)

    def _remove_player(self, old_player: Player) -> None:
        for index, player in enumerate(self.__players):
            correct_attrs = (
                player.name == old_player.name
                and player.health == old_player.health
                and player.weapon == old_player.weapon
                and player.level == old_player.level
            )
            if correct_attrs:
                self.__players.pop(index)
                return
        raise ValueError(f'{old_player.name} not in players')

    @property
    def weapons(self) -> list[Weapon]:
        """
        Getter for weapons.

        Returns:
            list[Weapon]: list with weapons.
        """
        return self.__weapons

    def _add_weapon(self, new_wepon: Weapon) -> None:
        if new_wepon in self.__weapons:
            raise ValueError('This weapon already exists')
        self.weapons.append(new_wepon)

    def _remove_weapon(self, old_weapon: Weapon) -> None:
        for index, weapon in enumerate(self.__weapons):
            correct_attrs = (
                weapon.name_weapon == old_weapon.name_weapon
                and weapon.damage == old_weapon.damage
            )
            if correct_attrs:
                self.__weapons.pop(index)
                return
        raise ValueError(f'{old_weapon.name} not in weapons')

    @property
    def enemies(self) -> list[Enemy]:
        """
        Getter for enemies.

        Returns:
            list[Enemy]: list with enemies.
        """
        return self.__enemies

    def _add_enemy(self, new_enemy: Enemy) -> None:
        if new_enemy in self.__enemies:
            raise ValueError('This enemy already exists')
        self.enemies.append(new_enemy)

    def _remove_enemy(self, old_enemy: Enemy) -> None:
        for index, enemy in enumerate(self.__enemies):
            correct_attrs = (
                enemy.name == old_enemy.name
                and enemy.health == old_enemy.health
                and enemy.weapon == old_enemy.weapon
            )
            if correct_attrs:
                self.__enemies.pop(index)
                return
        raise ValueError(f'{old_enemy.name} not in enemies')
