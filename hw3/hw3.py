"""A module for managing restaurant orders."""

from typing import Any, Callable


def ensure(attr: str, func: Callable) -> Callable:
    """
    Add property with specified checks to a class.

    Args:
        attr: Name of the attribute.
        func: function to check the attribute.

    Returns:
        Callable: Decorator function.
    """
    def add_property(class_name: type) -> type:
        """
        Add property to a Class.

        Args:
            class_name: Class to which property is added.

        Returns:
            type: Class with added property.
        """
        def getter(self) -> Any:
            """Getter method for retrieving the value of the specified attribute.

            Args:
                self: The instance of the class.

            Returns:
                Any: The value of the attribute.

            """
            return getattr(self, f'_{attr}')

        def setter(self, new_value) -> None:
            """Setter method for setting the value of the specified attribute.

            Args:
                self: The instance of the class.
                new_value: The value to be set for the attribute.
            """
            func(new_value)
            setattr(self, f'_{attr}', new_value)
        setattr(class_name, attr, property(getter, setter))
        return class_name
    return add_property


class Dish:
    """A class representing a dish.

    Attributes:
        name: The name of the dish.
        price: The price of the dish.
    """

    def __init__(self, name: str, price: int) -> None:
        """Initialize a Dish object with a name and price.

        Args:
            name: The name of the dish.
            price: The price of the dish.
        """
        self.name, self.price = name, price

    @property
    def name(self) -> str:
        """Getter method for obtaining the name of the dish.

        Returns:
            str: The name of the dish.
        """
        return self._name

    @property
    def price(self) -> int:
        """Getter method for obtaining the price of the dish.

        Returns:
            int: The price of the dish.
        """
        return self._price

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter method for setting the name of the dish.

        Args:
            new_name: The new name for the dish.

        Raises:
            TypeError: If the new_name is not of type str.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'Name {new_name} must be str, not {type(new_name).__name__}')
        self._name = new_name

    @price.setter
    def price(self, price: int) -> None:
        """Setter method for setting the price of the dish.

        Args:
            price: The new price for the dish.

        Raises:
            TypeError: If the price is not of type int.
            ValueError: If the price is less than or equal to 0.
        """
        if not isinstance(price, int):
            raise TypeError(f'Price {price} must be int, not {type(price).__name__}')
        if price <= 0:
            raise ValueError('Price must be positive')
        self._price = price


class Client:
    """A class representing a client.

    Attributes:
        name: The name of the client.
    """

    def __init__(self, name: str) -> None:
        """Initialize a Client object with a name.

        Args:
            name: The name of the client.
        """
        self.name = name

    @property
    def name(self) -> str:
        """Getter method for obtaining the name of the client.

        Returns:
            str: The name of the client.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter method for setting the name of the client.

        Args:
            new_name: The new name for the client.

        Raises:
            TypeError: If the new_name is not of type str.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'Name {new_name} must be str, not {type(new_name).__name__}')
        self._name = new_name


def check_list_of_dishes(list_of_dishes: list[Dish]):
    """Check if a list contains only objects of type Dish.

    Args:
        list_of_dishes: The list to be checked.

    Raises:
        TypeError: If the list_of_dishes is not of type list.
        ValueError: If the list contains an object that is not of type Dish.
    """
    if not isinstance(list_of_dishes, list):
        raise TypeError(f'{list_of_dishes} must be list, not {type(list_of_dishes).__name__}')
    for dish in list_of_dishes:
        if not isinstance(dish, Dish):
            raise ValueError(
                f'List must have only objects of class Dish, not {type(dish).__name__}',
            )


@ensure('list_of_dishes', check_list_of_dishes)
class Order:
    """A class representing an order placed by a client.

    Attributes:
        client: The client who placed the order.
        list_of_dishes: The list of dishes included in the order.
    """

    def __init__(self, client: Client, list_of_dishes: list[Dish]) -> None:
        """Initialize an Order object with a client and a list of dishes.

        Args:
            client: The client who placed the order.
            list_of_dishes: The list of dishes included in the order.
        """
        self.client, self.list_of_dishes = client, list_of_dishes

    @property
    def client(self) -> Client:
        """Getter method for obtaining the client of the order.

        Returns:
            Client: The client of the order.
        """
        return self._client

    @client.setter
    def client(self, new_client: Client) -> None:
        """Setter method for setting the client of the order.

        Args:
            new_client: The new client for the order.

        Raises:
            TypeError: If the new_client is not of type Client.
        """
        if not isinstance(new_client, Client):
            raise TypeError(f'{new_client} must be client, not {type(new_client).__name__}')
        self._client = new_client

    def add(self, dish: Dish) -> None:
        """Add a dish to the order's list of dishes.

        Args:
            dish: The dish to be added.

        Raises:
            ValueError: If the dish is already in the list of dishes.
        """
        if dish in self.list_of_dishes:
            raise ValueError(f'Dish {dish} is on the list')
        self.list_of_dishes.append(dish)

    def remove(self, dish: Dish) -> None:
        """Remove a dish from the order's list of dishes.

        Args:
            dish: The dish to be removed.

        Raises:
            ValueError: If the dish is not in the list of dishes.
        """
        if dish not in self.list_of_dishes:
            raise ValueError(f'Dish {dish} is not in list at the moment')
        self.list_of_dishes.remove(dish)

    def get_list(self) -> list[Dish]:
        """Get the list of dishes in the order.

        Returns:
            list: The list of dishes in the order.
        """
        return self.list_of_dishes


@ensure('available_dishes', check_list_of_dishes)
@ensure('all_dishes', check_list_of_dishes)
class Restaurant:
    """A class representing a restaurant.

    Attributes:
        orders: The list of orders placed at the restaurant.
        all_dishes: The list of all dishes offered by the restaurant.
        available_dishes: The list of currently available dishes at the restaurant.
    """

    def __init__(
        self,
        orders: list[Order],
        all_dishes: list[Dish],
        available_dishes: list[Dish],
    ) -> None:
        """Initialize a Restaurant object with a list of orders, all dishes, and available dishes.

        Args:
            orders: The list of orders placed at the restaurant.
            all_dishes: The list of all dishes offered by the restaurant.
            available_dishes: The list of currently available dishes at the restaurant.
        """
        self.all_dishes = all_dishes
        self.available_dishes = available_dishes
        self.orders = orders

    @property
    def orders(self) -> list[Order]:
        """Getter method for obtaining the list of orders at the restaurant.

        Returns:
            list: The list of orders at the restaurant.
        """
        return self._orders

    @orders.setter
    def orders(self, new_orders: list[Order]):
        """Setter method for setting the list of orders at the restaurant.

        Args:
            new_orders: The new list of orders.

        Raises:
            TypeError: If new_orders is not of type list.
            ValueError: If any object in new_orders is not of type Order.
            ValueError: If any object in order, which stores at new_orders, is not available dishes
        """
        if not isinstance(new_orders, list):
            raise TypeError(f'{new_orders} must be list, not {type(new_orders).__name__}')
        for order in new_orders:
            if not isinstance(order, Order):
                raise ValueError(
                    f'List must have only objects of class Order, not {type(order).__name__}',
                )

            if not all(dish in self.available_dishes for dish in order.list_of_dishes):
                raise ValueError(
                    f'Some dishes in order {order} is currently not available',
                )
        self._orders = new_orders

    def create_order(self, order: Order) -> None:
        """Create a new order at the restaurant.

        Args:
            order: The new order to be created.

        Raises:
            ValueError: If any dish in the order is not currently available.
        """
        for dish in order.list_of_dishes:
            if dish not in self.available_dishes:
                raise ValueError(f'Dish {dish} is currently not available')
        self.orders.append(order)

    def remove_order(self, order: Order) -> None:
        """Remove an order from the list of orders at the restaurant.

        Args:
            order: The order to be removed.

        Raises:
            ValueError: If the order is not in the list of orders.
        """
        if order not in self.orders:
            raise ValueError(f'Order {order} is not in list at the moment')
        self.orders.remove(order)

    def take_orders(self) -> list[Order]:
        """Get the list of orders at the restaurant.

        Returns:
            list: The list of orders at the restaurant.
        """
        return self.orders
