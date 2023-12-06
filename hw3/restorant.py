"""Thish module include class Restorant."""
from dish import Dish
from order import Order


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

    @property
    def av_dishes(self) -> list[Dish]:
        """Get av_dishes.

        Returns:
            list[Dish]: list with object type Dish
        """
        return self._av_dishes

    @av_dishes.setter
    def av_dishes(self, new_av: list[Dish]) -> None:
        """Set av_dishes.

        Args:
            new_av (list[Dish]): new avaible dishes

        Raises:
            TypeError: if type new_av not list | tuple or any values not object type Dish
            ValueError: _description_
        """
        if not isinstance(new_av, list | tuple):
            raise TypeError(f'{new_av} must be tiple[Dish] | list[Dish]')
        if any(not isinstance(dish, Dish) for dish in new_av):
            raise TypeError('All values must be object type Dish')
        if any(dish not in self.dishes for dish in new_av):
            raise ValueError('All values must be in dishes')
        self._av_dishes = new_av

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
        if any(dish not in self.av_dishes for dish in order.dishes):
            raise ValueError(f'{order.dishes} not avaible dish')
        self.orders.append(order)

    def remove_order(self, order_to_remove: Order) -> None:
        """Remove order in dishes.

        Args:
            order_to_remove (Order): order which we should remove
        """
        if order_to_remove in self.orders:
            self.orders.remove(order_to_remove)

    def get_order(self) -> str:
        """Get order as str.

        Returns:
            Order as str
        """
        return '\n'.join([f'{order.dishes} {order.clients}' for order in self.orders])
