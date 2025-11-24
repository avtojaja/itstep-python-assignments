# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Output: (5, 7)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ვექტორების დამატება
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # სტრინგის ფორმატირება
    def __str__(self):
        return f"({self.x}, {self.y})"


# მაგალითი
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)



# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი, რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად, თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # გადატვირთული ტოლობის ოპერატორი
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

# მაგალითი
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False



# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.
# Car კლასს დაუმატეთ თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.
# დაამატეთ Car კლასის set ფუნქციებში ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის მთელი და ა.შ.

from datetime import datetime

class Car:
    def __new__(cls, *args, **kwargs):
        # __new__ გამოიყენება ახალი ობიექტის შექმნისთვის
        instance = super().__new__(cls)
        print("Creating a new Car instance...")
        return instance

    def __init__(self, brand, model, year):
        # __init__ ინიციალიზაციას ახდენს
        self.brand = brand
        self.model = model
        self.year = year

    # brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    # model property
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._model = value

    # year property
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.now().year
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        if value < 1886 or value > current_year: # 1886 წელს გამოუშვეს პირველი ავტომობილი
            raise ValueError(f"Year must be between 1886 and {current_year}")
        self._year = value

    # ფუნქცია ავტომობილის დეტალების დასაბეჭდად
    def car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# მაგალითი
try:
    car1 = Car("Toyota", "Corolla", 2020)
    car1.car_info()
    # car1.year = "2020"  # ValueError
    # car1.brand = 123    # ValueError
    car2 = Car("FutureCar", "X1", 2050)  # ValueError
except ValueError as e:
    print(f"Error: {e}")
