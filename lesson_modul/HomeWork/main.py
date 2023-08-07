
from cart_product import Product, Cart
from menu_discount import Dish, Category, Menu, Order


if __name__ == '__main__':
    pr1 = Product('apple', 30)
    pr2 = Product('apple lux', 60)
    pr3 = Product('banana', 50)
    pr4 = Product('orange', 40)

    cart = Cart()
    cart.add_product(pr1, 4)
    cart.add_product(pr4, 2)
    cart.add_product(pr3, 3)
    cart.add_product(pr2, 5)

    dish1 = Dish('cheesecake1', 'description 1', 100)
    dish2 = Dish('cheesecake2', 'description 2', 101)
    dish3 = Dish('cheesecake3', 'description 3', 102)
    dish4 = Dish('cheesecake4', 'description 4', 103)


    cat1 = Category('category1')
    cat2 = Category('category2')

    cat1.add_dish(dish1)
    cat1.add_dish(dish2)
    cat2.add_dish(dish3)
    cat2.add_dish(dish4)


    menu = Menu()
    menu.add_category(cat1)
    menu.add_category(cat2)

    order = Order()
    order.add_dish(dish1)
    order.add_dish(dish2)


    print(cart)
    print(menu)
    print(order)
    print()


