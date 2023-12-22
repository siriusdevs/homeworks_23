"""Module for Dish class."""


from product import Product


class Dish:
    """Class Dish. It can add and remove products."""

    __pool = {}

    def __new__(cls, dish_name: str, products: list[Product]):
        """Create Dish with flyweight.

        Args:
            dish_name (str): a dish name
            products (list[Product]): products in the dish

        Returns:
            Self: class <Dish>
        """
        args_key = f'{dish_name}-{products}'
        if args_key not in cls.__pool.keys():
            cls.__pool[args_key] = super().__new__(cls)
        return cls.__pool[args_key]

    def __init__(self, dish_name: str, products: list[Product]) -> None:
        """Init for Dish.

        Args:
            dish_name (str): a dish name
            products (list[Product]): products in the dish
        """
        self.dish_name, self.products = dish_name, products

    def __str__(self) -> str:
        """Make a str view for Dish.

        Returns:
            str: a str view for Dish
        """
        return f'Dish {self.dish_name}-{self.products}'

    @property
    def dish_name(self):
        """Getter for a dish name.

        Returns:
            str: the dish name
        """
        return self.__dish_name

    @dish_name.setter
    def dish_name(self, new_dish_name: str):
        """Setter for a dish name.

        Args:
            new_dish_name (str): a new dish name

        Raises:
            TypeError: raise if new dish name is not <str>
        """
        if not isinstance(new_dish_name, str):
            raise TypeError('new_dish_name must be <str> !')
        self.__dish_name = new_dish_name

    @property
    def products(self):
        """Getter for products.

        Returns:
            list[Product]: the products.
        """
        return self.__products

    @products.setter
    def products(self, new_products: list[Product]):
        """Setter for products.

        Args:
            new_products (list[Product]): new products

        Raises:
            TypeError: raise if new products are not list
            TypeError: raise all new products are not <Product>
        """
        if not isinstance(new_products, list):
            raise TypeError('new_products must be list!')
        for new_product in new_products:
            if not isinstance(new_product, Product):
                raise TypeError('All products must be <Product> !')
        self.__products = new_products

    def add_product(self, product: Product):
        """Add product.

        Args:
            product (Product): a product

        Raises:
            TypeError: raise if product is not <Product>
        """
        if not isinstance(product, Product):
            raise TypeError('product must be <Product> !')
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove product.

        Args:
            product (Product): a product

        Raises:
            TypeError: raise if product if not <Product>
        """
        if not isinstance(product, Product):
            raise TypeError('product must be <Product> !')
        self.products.remove(product)
