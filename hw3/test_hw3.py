"""Файл тестирования классов."""
import unittest

from hw3.hw3 import Dish, Product, Restaurant


class TestRestaurantClasses(unittest.TestCase):
    """Тесты для классов Product, Dish и Restaurant."""

    def setUp(self):
        """Настройка перед выполнением каждого теста."""
        self.product1 = Product('Яблоко', 1.0)
        self.product2 = Product('Банан', 2.0)

        self.dish = Dish('Фруктовый салат')
        self.dish.add_product(self.product1)
        self.dish.add_product(self.product2)

        self.restaurant = Restaurant(
            'Наш ресторан', [self.dish], [self.product1, self.product2]
        )

    def test_product_attributes(self):
        """Проверка атрибутов продукта."""
        self.assertEqual(self.product1.name, 'Яблоко')
        self.assertEqual(self.product1.price, 1.0)

    def test_dish_attributes(self):
        """Проверка атрибутов блюда."""
        self.assertEqual(self.dish.name, 'Фруктовый салат')
        self.assertEqual(len(self.dish.products), 2)

    def test_restaurant_attributes(self):
        """Проверка атрибутов ресторана."""
        self.assertEqual(self.restaurant.name, 'Наш ресторан')
        self.assertEqual(len(self.restaurant.dishes), 1)
        self.assertEqual(len(self.restaurant.inventory), 2)

    def test_add_and_remove_dish_from_menu(self):
        """Проверка добавления и удаления блюда из меню ресторана."""
        new_dish = Dish('Суп')
        self.restaurant.add_dish(new_dish)
        self.assertIn(new_dish, self.restaurant.dishes)
        self.restaurant.remove_dish(new_dish)
        self.assertNotIn(new_dish, self.restaurant.dishes)

    def test_add_and_remove_product_from_dish(self):
        """Проверка добавления и удаления продукта из блюда."""
        new_product = Product('Апельсин', 1.5)
        self.dish.add_product(new_product)
        self.assertIn(new_product, self.dish.products)
        self.dish.remove_product(new_product)
        self.assertNotIn(new_product, self.dish.products)

    def test_order_dish_with_available_inventory(self):
        """Проверка успешного заказа блюда с доступным инвентарем."""
        result = self.restaurant.order_dish(self.dish)
        self.assertEqual(result, 'Блюдо заказано успешно')
        self.assertEqual(len(self.restaurant.inventory), 0)

    def test_order_dish_without_enough_inventory(self):
        """Проверка заказа блюда без достаточного инвентаря."""
        self.restaurant.order_dish(self.dish)
        result = self.restaurant.order_dish(self.dish)
        self.assertEqual(result, 'Не хватает товаров на складе')
        self.assertEqual(len(self.restaurant.inventory), 0)


if __name__ == "__main__":
    unittest.main()
