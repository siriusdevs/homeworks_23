"""Module for Product class."""


class Product:
    """Class for products."""

    __pool = {}

    def __new__(cls, product_name: str, product_price: float | int):
        """Create a product with flyweight.

        Args:
            product_name (str): a product name
            product_price (float | int): a product price

        Returns:
            Self: class <Product>
        """
        args_key = f'{product_name}-{product_price}'
        if args_key not in cls.__pool.keys():
            cls.__pool[args_key] = super().__new__(cls)
        return cls.__pool[args_key]

    def __init__(self, product_name: str, product_price: float | int) -> None:
        """Init a product.

        Args:
            product_name (str): a product name
            product_price (float | int): a product price
        """
        self.product_name, self.product_price = product_name, product_price

    def __str__(self) -> str:
        """Make a str view for Product.

        Returns:
            str: A str view for product
        """
        return f'Product name_product={self.product_name}, price_product={self.product_price}'

    @property
    def product_name(self):
        """Getter for product name.

        Returns:
            str: a product name
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, new_product_name: str):
        """Setter for product_name.

        Args:
            new_product_name (str): a new product name

        Raises:
            TypeError: raise if a new name product is not str
        """
        if not isinstance(new_product_name, str):
            raise TypeError('new_name_product must be <str>!')
        self.__product_name = new_product_name

    @property
    def product_price(self):
        """Getter for product_price.

        Returns:
            float | int: a product price
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, new_product_price: float | int):
        """Setter for product price.

        Args:
            new_product_price (float | int): a new product price

        Raises:
            TypeError: raises if new product price has invalid type
            ValueError: raise if new product price is less than 0
        """
        if not isinstance(new_product_price, float | int):
            raise TypeError('new_price_product must be <float | int>!')
        if new_product_price < 0:
            raise ValueError('new_price_product must be > 0 !')
        self.__product_price = new_product_price
