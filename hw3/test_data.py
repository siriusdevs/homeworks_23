"""This module incliding data for test."""
from client import Client
from dish import Dish
from order import Order

names_of_clients = ('Albert', 'Artem')
names_price_of_dish = (('Eggs', 350), ('Ice cream', 120))
clients = ([[Client('Albert')], [Dish('Tomato', 5)]], )
add_remove_dishes = (Dish('Toast', 4), Dish('Ice Cream', 2), Dish('Popcorn', 9))
order = Order([Client('Albert')], [Dish('Waffles', 5)])
test_getdishnames_data = ((
    Order([Client('Anna')], [Dish('Waffles', 5), Dish('Ice Cream', 2)]), 'Waffles, Ice Cream',
),
    (
    Order([Client('Artem')], [Dish('Toast', 5), Dish('Ice Cream', 2)]), 'Toast, Ice Cream',
))

test_data = ((
    [order],
    [Dish('Rice', 5), Dish('Cheeze', 10), Dish('Water', 5)],
    [Dish('Water', 5), Dish('Rice', 5)],
),
)
