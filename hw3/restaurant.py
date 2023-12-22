"""Module for Restaurant class."""


from dish import Dish
from product import Product


class Restaurant:
    """Class Restaurant. It can order a dish, remove products, add products and the like."""

    def __init__(self, name_restaurant: str, suggest_dishes: set[Dish], products: list[Product]):
        """Init for Restaurant.

        Args:
            name_restaurant (str): a restaurant name
            suggest_dishes (set[Dish]): suggest dishes in the restaurant
            products (list[Product]): products that restaurant has
        """
        self.restaurant_name = name_restaurant
        self.suggest_dishes = suggest_dishes
        self.products = products

    @property
    def restaurant_name(self):
        """Getter for restaurant name.

        Returns:
            str: the restaurant name
        """
        return self.__restaurant_name

    @restaurant_name.setter
    def restaurant_name(self, new_name: str):
        """Setter for restaurant name.

        Args:
            new_name (str): a new restaurant name

        Raises:
            TypeError: raise if new_name is not str
        """
        if not isinstance(new_name, str):
            raise TypeError('new_name must be <str> !')
        self.__restaurant_name = new_name

    @property
    def suggest_dishes(self):
        """Getter for suggest dishes.

        Returns:
            set[Dish]: suggesting dishes
        """
        return self.__suggest_dishes

    @suggest_dishes.setter
    def suggest_dishes(self, new_dishes: set[Dish]):
        """Setter for suggest dishes.

        Args:
            new_dishes (set[Dish]): new dishes

        Raises:
            TypeError: raise if new dishes are not set
            TypeError: raise if all new dishes are not <Dish>
        """
        if not isinstance(new_dishes, set):
            raise TypeError('All dishes are unique, they must be <set>!')
        for dish in new_dishes:
            if not isinstance(dish, Dish):
                raise TypeError('All dishes must be <Dish> !')
        self.__suggest_dishes = new_dishes

    @property
    def products(self):
        """Getter for products.

        Returns:
            list[Product]: the products
        """
        return self.__products

    @products.setter
    def products(self, new_products: list[Product]):
        """Setter for products.

        Args:
            new_products (list[Product]): new products
        """
        self.__check_type_products(new_products)
        self.__products = new_products

    def remove_products(self, removing_products: list[Product]):
        """Remove products.

        Args:
            removing_products (list[Product]): products that we remove
        """
        self.__check_type_products(removing_products)
        for removing_product in removing_products:
            self.products.remove(removing_product)

    def add_dish(self, dish: Dish):
        """Add a dish.

        Args:
            dish (Dish): a dish

        Raises:
            TypeError: raise if dish is not <Dish>
        """
        if not isinstance(dish, Dish):
            raise TypeError('dish must be <Dish> !')
        self.suggest_dishes.add(dish)

    def remove_dish(self, dish: Dish):
        """Remove a dish.

        Args:
            dish (Dish): a dish

        Raises:
            TypeError: raise if dish is not <Dish>
        """
        if not isinstance(dish, Dish):
            raise TypeError('dish must be <Dish> !')
        self.suggest_dishes.remove(dish)

    def order_dish(self, order_dish: Dish) -> Dish | None:
        """Order dish if it is possible.

        Args:
            order_dish (Dish): a order dish

        Raises:
            TypeError: raise if order_dish is not <Dish>

        Returns:
            Dish | None: If restaurant has products return Dish else None
        """
        if not isinstance(order_dish, Dish):
            raise TypeError('dish must be <Dish> !')

        if not self.products or order_dish not in self.suggest_dishes:
            return None

        if set(order_dish.products).issubset(self.products):
            self.remove_products(order_dish.products)
            return order_dish

        return None

    def __check_type_products(self, products: list[Product]):
        """Check type of products.

        Args:
            products (list[Product]): the products

        Raises:
            TypeError: raise if products are not list
            TypeError: raise if all products are not <Product>
        """
        if not isinstance(products, list):
            raise TypeError('products must be list!')
        for product in products:
            if not isinstance(product, Product):
                raise TypeError('new_product must be <Product> !')
