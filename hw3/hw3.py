"""This module include class architecture for managing orders in a restaurant."""

from typing import Any


class Client:
    """This class describes Client."""

    def __init__(self, name: str) -> None:
        """Init class Client.

        Args:
            name (str): Name of client
        """
        self.name = name

    @property
    def name(self) -> str:
        """Get name.

        Returns:
            Name of client.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set name.

        Args:
            new_name (str): new client name

        Raises:
            TypeError: if new_name not str
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{new_name} must be str')
        self._name = new_name

    def __repr__(self) -> str:
        """Return a string representation of the object for debugging.

        Returns:
            str:  A string representation of the object.
        """
        return f'{self.name}'


def checker(attrs: str, object_type: Any) -> None:
    """Add setter and getter for class.

    Args:
        attrs (str): name of attribute
        object_type (Any): type of object, which nedd to be check

    Returns:
        function of decorator
    """
    def decorator(cls):
        """Add setter and getter for class.

        Args:
            cls: class which we convey

        Returns:
            Class which we convey
        """

        def getter(self) -> list[Any]:
            """Get attrs.

            Args:
                self: instance of class

            Returns:
                _attr
            """
            return getattr(self, f'_{attrs}')

        def settter(self, new_values):
            """Set attrs.

            Args:
                new_values (_type_): _description_
                self: instance of class

            Raises:
                TypeError: if type of attrs does not match object_type
            """
            if not isinstance(new_values, list | tuple):
                raise TypeError(f'{new_values} must be list or float')
            if any(not isinstance(veriable, object_type) for veriable in new_values):
                raise TypeError(f'All value must be object type {object_type.__name__}')
            setattr(self, f'_{attrs}', new_values)
        prop = property(getter, settter)
        setattr(cls, attrs, prop)
        return cls
    return decorator


class Dish:
    """This class describe dish."""

    def __init__(self, name_dish: str, price: int | float) -> None:
        """Init the class Dish.

        Args:
            name_dish (str): name of dish
            price (int | float): price of dish
        """
        self.name_dish, self.price = name_dish, price

    @property
    def name_dish(self) -> str:
        """Get name_dish.

        Returns:
            str: name_dish
        """
        return self._name_dish

    @name_dish.setter
    def name_dish(self, new_dish: str) -> None:
        """Set name_dish.

        Args:
            new_dish (str): new name dish

        Raises:
            TypeError: if type of new_dish not str
        """
        if not isinstance(new_dish, str):
            raise TypeError(f'{new_dish} must be str')
        self._name_dish = new_dish

    @property
    def price(self) -> int | float:
        """Get price.

        Returns:
            Price of dish
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Set price.

        Args:
            new_price (int | float): new price of dish

        Raises:
            TypeError: if type of new_price not int or float
        """
        if not isinstance(new_price, int | float):
            raise TypeError(f'{new_price} must be a number')
        self._price = new_price

    def __repr__(self) -> str:
        """Return a string representation of the object for debugging.

        Returns:
            str:  A string representation of the object.
        """
        return f'{self.name_dish}: {self.price}'


@checker('clients', Client)
@checker('dishes', Dish)
class Order:
    """This class discribe order."""

    def __init__(self, clients: list[Client], dishes: list[Dish]) -> None:
        """Init the class Order.

        Args:
            clients (list[Client]): list of object type Client
            dishes (list[Dish]): list of object type Dish
        """
        self.clients, self.dishes = clients, dishes

    def add_dish(self, new_dish: Dish) -> None:
        """Add dishes new dish.

        Args:
            new_dish (Dish): dish object type Dish

        Raises:
            TypeError: if type of new_dish not Dish
        """
        if not isinstance(new_dish, Dish):
            raise TypeError(f'{new_dish} must be object Dish')
        self.dishes.append(new_dish)

    def remove_dishes(self, remove_dish: Dish) -> None:
        """Remove dish from dishes.

        Args:
            remove_dish (Dish): dish which we should remove
        """
        if remove_dish in self.dishes:
            self.dishes.remove(remove_dish)

    def get_dishname(self) -> str:
        """Get dishname as str.

        Returns:
            Dishname as str
        """
        return ', '.join(dish.name_dish for dish in self.dishes)


@checker('orders', Order)
@checker('dishes', Dish)
@checker('av_dishes', Dish)
class Restorant:
    """This class discribe restorant."""

    def __init__(self, orders: list[Order], dishes: list[Dish], av_dishes: list[Dish]) -> None:
        """Init the class Restorant.

        Args:
            orders (list[Order]): order list
            dishes (list[Dish]): dishes list
            av_dishes (list[Dish]): avaible dishes list
        """
        self.orders, self.dishes, self.av_dishes = orders, dishes, av_dishes

    def make_order(self, order: Order) -> None:
        """Add new order to orders.

        Args:
            order (Order): object type Order

        Raises:
            TypeError: if type of client not Client
            ValueError: if any in new_dishes not in dishes
        """
        if not isinstance(order, Order):
            raise TypeError(f'{order} must be object type Order')
        if order.dishes in self.av_dishes:
            raise ValueError(f'{order.dishes} not avaible dish')
        self.orders.append(order)

    def remove_order(self, order_to_remove: Dish) -> None:
        """Remove order in dishes.

        Args:
            order_to_remove (Dish): dish which we should remove
        """
        if order_to_remove in self.orders:
            self.orders.remove(order_to_remove)

    def get_order(self) -> str:
        """Get order as str.

        Returns:
            Order as str
        """
        return ', '.join([f'{dish.name_dish}: {dish.price}' for dish in self.dishes])
