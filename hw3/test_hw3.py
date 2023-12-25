"""Файл тестирования классов."""
import unittest

from hw3 import Dish, MenuManager, Product, RestaurantDetails

BANANA_PRICE = 2.0
ORANGE_PRICE = 1.5
PIZZA = 'Pizza'
PASTA = 'Pasta'


class TestRestaurantClasses(unittest.TestCase):
    """Тесты для классов Product, Dish и Restaurant."""

    def setUp(self):
        """Настройка перед выполнением каждого теста."""
        self.product1 = Product('Яблоко', 1.0)
        self.product2 = Product('Банан', BANANA_PRICE)

        self.dish = Dish('Фруктовый салат')
        self.dish.add_product(self.product1)
        self.dish.add_product(self.product2)

        self.restaurant_details = RestaurantDetails('Test Restaurant', [PIZZA, PASTA])

    def test_product_attributes(self):
        """Проверка атрибутов продукта."""
        self.assertEqual(self.product1.name, 'Яблоко')
        self.assertEqual(self.product1.price, 1.0)

    def test_dish_attributes(self):
        """Проверка атрибутов блюда."""
        self.assertEqual(self.dish.name, 'Фруктовый салат')
        self.assertEqual(len(self.dish.products), 2)

    def test_add_and_remove_product_from_dish(self):
        """Проверка добавления и удаления продукта из блюда."""
        new_product = Product('Апельсин', ORANGE_PRICE)
        self.dish.add_product(new_product)
        self.assertIn(new_product, self.dish.products)
        self.dish.remove_product(new_product)
        self.assertNotIn(new_product, self.dish.products)


class TestRestaurantDetails(unittest.TestCase):
    """Класс тестирования параметров ресторана."""
    
    def setUp(self):
        """Метод инициализации перед тестированием."""
        self.restaurant_details = RestaurantDetails('Test Restaurant', [PIZZA, PASTA])

    def test_name(self):
        """Проверка имени."""
        self.assertEqual(self.restaurant_details.name, 'Test Restaurant')

    def test_inventory(self):
        """Проверка продуктов для блюда."""
        self.assertEqual(self.restaurant_details.inventory, [PIZZA, PASTA])

    def test_set_name(self):
        """Проверка сеттера имени."""
        self.restaurant_details.name = 'New Name'
        self.assertEqual(self.restaurant_details.name, 'New Name')


class TestMenuManager(unittest.TestCase):
    """Класс тестирования функционала."""
    
    def setUp(self):
        """Метод инициализации перед тестами."""
        self.menu_manager = MenuManager([PIZZA, PASTA])

    def test_dishes(self):
        """Тестирование блюд."""
        self.assertEqual(self.menu_manager.dishes, [PIZZA, PASTA])

    def test_add_dish(self):
        """Тест добавления блюда."""
        self.menu_manager.add_dish('Salad')
        self.assertEqual(self.menu_manager.dishes, [PIZZA, PASTA, 'Salad'])

    def test_remove_dish(self):
        """Тест удаления блюда."""
        self.menu_manager.remove_dish(PIZZA)
        self.assertEqual(self.menu_manager.dishes, [PASTA])


if __name__ == '__main__':
    unittest.main()
