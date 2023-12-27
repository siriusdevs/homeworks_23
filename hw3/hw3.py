"""This is solution for hw3."""


class Client:
    """Instance of a client."""

    def __init__(self, name: str) -> None:
        """Client instance initialization.

        Args:
            name: str - name of client.
        """
        self.name = name

    @property
    def name(self) -> str:
        """Getter for the name property of the instance.

        Returns:
            str: name of client..
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter for the name property of the instance.

        Args:
            new_name: str - new title of dish.

        Raises:
            TypeError: if not str given.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{type(new_name).__name__} is not str')
        self._name = new_name


class Dish:
    """Instance of a dish."""

    def __init__(self, name: str, price: int | float) -> None:
        """Dish instance initialization.

        Args:
            name: str - title of dish.
            price: (int | float) - price of dish.
        """
        self.name, self.price = name, price

    @property
    def name(self) -> str:
        """Getter for the name property of the instance.

        Returns:
            str: title of dish.
        """
        return self._name

    @property
    def price(self) -> int | float:
        """Getter for the price property of the instance.

        Returns:
            int | float: price of dish.
        """
        return self._price

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter for the name property of the instance.

        Args:
            new_name: str - new title of dish.

        Raises:
            TypeError: if not str given.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{type(new_name).__name__} is not str')
        self._name = new_name

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Setter for the price property of the instance.

        Args:
            new_price: (int | float) - new price of dish.

        Raises:
            TypeError: if not numeric given.
            ValueError: if not positive given.
        """
        if not isinstance(new_price, (int, float)):
            raise TypeError(f'{type(new_price).__name__} is not float or int')
        if new_price < 0:
            raise ValueError(f'{new_price} should be positive')
        self._price = new_price


class DishMethods(Dish):
    """Dish methods."""

    def __str__(self) -> str:
        """Visualisaion of instance in string.

        Returns:
            str: representation of instance.
        """
        return f'{self.__class__.__name__} with price: {self.price}'


class Order:
    """Order instance."""

    def __init__(self, client: Client, dishes: list[Dish]):
        """Order instance initialization.

        Args:
            client: Client - Client class object.
            dishes: list[Dish] - dishes on order.
        """
        self.client, self.dishes = client, dishes

    @property
    def client(self) -> Client:
        """Getter for the client property of the instance.

        Returns:
            Client: Client class object
        """
        return self._client

    @property
    def dishes(self) -> list[Dish]:
        """Getter for the dishes property of the instance.

        Returns:
            list[Dish]: dishes on order.
        """
        return self._dishes

    @client.setter
    def client(self, new_client: Client) -> None:
        """Setter for the client property of the instance.

        Args:
            new_client: Client - new Client class object.

        Raises:
            TypeError: if not Client given.
        """
        if not isinstance(new_client, Client):
            raise TypeError(f'{type(new_client).__name__} was given instead of Client')
        self._client = new_client

    @dishes.setter
    def dishes(self, new_dishes: list[Dish]) -> None:
        """Setter for the dishes property of the instance.

        Args:
            new_dishes: list[Dish] - new dishes on order.

        Raises:
            TypeError: if not list given.
            TypeError: if not Dish value in tuple given.
        """
        if not isinstance(new_dishes, list):
            raise TypeError(f'{type(new_dishes).__name__} is not list')
        for dish in new_dishes:
            if not isinstance(dish, Dish):
                raise TypeError(f'{type(dish).__name__} was given instead of Dish')
        self._dishes = new_dishes


class OrderMethods(Order):
    """Order methods."""

    def add_dish(self, dish: Dish) -> None:
        """Add dish in order.

        Args:
            dish: Dish - Dish class object.

        Raises:
            TypeError: if not Dish given.
        """
        if not isinstance(dish, Dish):
            raise TypeError(f'{type(dish).__name__} was given instead of Dish')
        self._dishes.append(dish)

    def remove_dish(self, dish: Dish) -> None:
        """Remove dish in order.

        Args:
            dish: Dish - Dish class object.

        Raises:
            ValueError: if object not in the list.
        """
        if dish not in self._dishes:
            raise ValueError(f'You cannot delete {dish} because it is not in the list')
        self._dishes.remove(dish)

    def get_dishes(self) -> list[Dish]:
        """Fun function to get dish in the order.

        Returns:
            list[Dish]: dish in the order.
        """
        return self._dishes

    def __str__(self) -> str:
        """Visualisaion of instance in string.

        Returns:
            str: representation of instance.
        """
        return f'{self.__class__.__name__} recipient: {self.client} \
composition of the order: {self.dishes}'


class Restaurant:
    """Restaurant instance."""

    def __init__(
        self,
        orders: list[Order],
        all_dishes: list[Dish],
        available_dishes: list[Dish],
    ) -> None:
        """Restaurant instance initialization.

        Args:
            orders: list[Order] - all orders.
            all_dishes: list[Dish] - menu of restaurant.
            available_dishes: list[Dish] - available dishes in restaurant.
        """
        self.orders, self.all_dishes, self.available_dishes = orders, all_dishes, available_dishes

    @property
    def orders(self) -> list[Order]:
        """Getter for the orders property of the instance.

        Returns:
            list[Order]: all orders.
        """
        return self._orders

    @property
    def all_dishes(self) -> list[Dish]:
        """Getter for the all dishes property of the instance.

        Returns:
            list[Dish]: menu of restaurant.
        """
        return self._all_dishes

    @property
    def available_dishes(self) -> list[Dish]:
        """Getter for the available dishes property of the instance.

        Returns:
            list[Dish]: available dishes in restaurant.
        """
        return self._available_dishes

    @orders.setter
    def orders(self, new_orders: list[Order]) -> None:
        """Setter for the orders property of the instance.

        Args:
            new_orders: list[Order] - new all orders.

        Raises:
            TypeError: if not list diven.
            TypeError: if not Dish value in list given.
        """
        if not isinstance(new_orders, list):
            raise TypeError(f'{type(new_orders).__name__} is not list')
        for order in new_orders:
            if not isinstance(order, Order):
                raise TypeError(f'{type(order).__name__} was given instead of Order')
        self._orders = new_orders

    @all_dishes.setter
    def all_dishes(self, new_all_dishes: list[Dish]) -> None:
        """Setter for the all dishes property of the instance.

        Args:
            new_all_dishes: list[Dish] - new menu of restaurant.

        Raises:
            TypeError: if not list given.
            TypeError: if not Dish value in list given.
        """
        if not isinstance(new_all_dishes, list):
            raise TypeError(f'{type(new_all_dishes).__name__} should be list')
        for dish in new_all_dishes:
            if not isinstance(dish, Dish):
                raise TypeError(f'{type(dish).__name__} was given instead of Dish')
        self._all_dishes = new_all_dishes

    @available_dishes.setter
    def available_dishes(self, new_available_dishes: list[Dish]) -> None:
        """Setter for the available dishes property of the instance.

        Args:
            new_available_dishes: list[Dish] - new available dishes in restaurant.

        Raises:
            TypeError: if not list given.
            TypeError: if not Dish value in list given.
        """
        if not isinstance(new_available_dishes, list):
            raise TypeError(f'{type(new_available_dishes).__name__} is not list')
        for dish in new_available_dishes:
            if not isinstance(dish, Dish):
                raise TypeError(f'{type(dish).__name__} should be Dish')
        self._available_dishes = new_available_dishes


class RestaurantMethods(Restaurant):
    """Restaurant methods."""

    def create_order(self, client: Client, order_dishes: list[Dish]) -> Order:
        """Create an order.

        Args:
            client: Client - Client class object.
            order_dishes: list[Dish] - dish in order.

        Returns:
            Order: Order class object.
        """
        if all(dish in self.available_dishes for dish in order_dishes):
            order = Order(client, order_dishes)
            self._orders.append(order)
            return order

        return 'Not all dishes are available.'

    def remove_order(self, order: Order) -> None:
        """Remove order.

        Args:
            order: Order - Order class object.

        Raises:
            ValueError: if object not in the list.
        """
        if order not in self._orders:
            raise ValueError(f'You cannot delete {order} because it is not in the list')
        self._orders.remove(order)

    def get_orders(self) -> list:
        """Fun function to get all orders.

        Returns:
            list: all orders.
        """
        return self._orders

    def __str__(self) -> str:
        """Visualisaion of instance in string.

        Returns:
            str:  representation of instance.
        """
        name = self.__class__.__name__
        dishes = self.all_dishes
        avalable_dishes = self.available_dishes
        return f'Menu {name}: {dishes}, available dishes: {avalable_dishes}'
