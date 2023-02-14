import hashlib
import re
import random


class IdCounter:
    def __init__(self):
        self.id_ = 0

    def get_id_(self):
        self.id_ += 1
        return self.id_


class Password:
    def __init__(self):
        self.password = None

    def get_hash(self, password: input):
        self.password = input("Введите пароль от учетной записи\n")
        pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if len(self.password) > 8:
            if re.match(pattern2, self.password) is True:
                self.password = password
            elif re.match(pattern2, self.password) is False:
                print("Пароль должен содержать символы и цифры")
        elif len(password) < 8:
            print("Пароль должен быть длиннее трех символов")
        password = hashlib.sha256(password.encode()).hexdigest()
        return password

    def check_password(self, old_hash, password):
        if old_hash == hashlib.sha256(password.encode()).hexdigest():
            if password == hashlib.sha256(password.encode()).hexdigest():
                print("Авторизация прошла успешно")
            else:
                print("Пароль неверный")


class Product:
    id_counter = IdCounter()

    def __init__(self, name, price, rating):
        self._id = self.id_counter.get_id_()
        self._name = name
        self.price = price
        self.rating = rating

        # @property
        # def id_(self):
        #     super().id_()
        #     return self._id_ = _id_

    @property
    def name(self):
        return self._name

    def get_price(self):
        return f'{self.price}'

    def set_price(self, price):
        if not isinstance(price, int):
            raise TypeError("Цена должна быть целым числом")
        elif price < 0:
            raise ValueError("Цена должна быть больше нуля")
        else:
            self.price = price

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        if not isinstance(rating, int):
            raise TypeError("Рейтинг должен быть целым числом")
        elif 0 > rating >= 5:
            raise ValueError("Рейтинг может быть от 1 до 5")
        else:
            self.rating = rating

    def __str__(self):
        print(f'{self._id}_{self.name}_{self.price}_{self.rating}')

    def __repr__(self):
        print(f'{self._id}_{self.name}_{self.price}_{self.rating}')


class Cart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def del_from_cart(self, product):
        self.cart.remove(product)

    def __str__(self):
        return f'{self.cart}'

    def __repr__(self):
        return f'{self.cart}'


class User:
    id_counter = IdCounter()
    user_password = Password()

    def __init__(self, username, password):
        self._id = self.id_counter.get_id_()
        self.user_cart = Cart()
        self.cart_ = self.user_cart.cart
        self.__password = self.user_password.get_hash(password)
        if len(username) > 3:
            if isinstance(username, str):
                self._username = username

    @property
    def username(self):
        return self._username

    def __str__(self):
        print(f'{self._id}_{self.username}_"password1"')

    def __repr__(self):
        print(f'{self._id}_{self.username}_"password1"')


class Store:
    # user_password = Password()
    # user_cart = Cart()

    def __init__(self):
        self.user = None
        self.auth()
        # self.user_cart = Cart()
        # self.__password = self.user_password.get_hash(input())

    def auth(self):
        self.login = input("Введите логин\n")
        self.user = User(self.login, password=input("Введите пароль"))

    def add_random_product(self):
        random_product = random.choice(open('products.txt', encoding="utf-8").readlines())
        self.user.user_cart.add_to_cart(random_product)
        return f'{self.user.user_cart}'

    def get_user_cart(self):
        print(self.user.user_cart)


if __name__ == '__main__':
    """Тест класса "Продукт" """
    product1 = Product("Name1", "2000", "5")
    product2 = Product("Name2", "3000", "1")
    # product1.__str__()
    # product1.set_rating(4)
    # product1.__str__()
    # product2.set_price(0)
    # product2.__str__()

    """Тест добавления продуктов в корзину и отображения корзины """
    # store = Store()
    # store.add_random_product()
    # print(store.user_cart)
    # store.add_random_product()
    # print(store.user_cart)

    """Тест класса "Корзина" """
    cart = Cart()
    cart.add_to_cart(product1)
    cart.__str__()
