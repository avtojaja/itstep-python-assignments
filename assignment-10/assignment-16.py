# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

from datetime import datetime

class Car:
    # 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას.
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        # რაოდენობის ზრდა ყოველი ახალი მანქანის შექმნისას
        Car.number_of_cars += 1

    # 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.
    def age_of_car(self):
        current_year = datetime.now().year
        return current_year - self.year

    def car_info(self):
        print(f"ბრენდი: {self.brand}")
        print(f"მოდელი: {self.model}")
        print(f"გამოშვების წელი: {self.year}")
        print(f"ავტომობილის ასაკი: {self.age_of_car()} წლის")

    # 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.
    @classmethod
    def total_cars(cls):
        print(f"ავტომობილების რაოდენობა: {cls.number_of_cars}")

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)  # კონსტრუქტორის მემკვიდრეობით გადაცემის უზრუნველყოფა
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")


# მაგალითი
car1 = Car("Toyota", "Corolla", 2015)
car2 = ElectricCar("Tesla", "Model S", 2022, 12)

car1.car_info()
print()
car2.car_info()
car2.battery_info()
print()
Car.total_cars()
