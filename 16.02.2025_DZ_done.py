# Создайте систему учета транспортных средств с использованием следующих концепций ООП: инкапсуляция,
# абстрактный класс и перегрузка методов. Классы должны позволять хранить данные о транспортных средствах и
# предоставлять методы для расчета налогов в зависимости от типа транспорта.
#
# Требования:
# 1	Абстрактный класс Vehicle:
# ◦	Поля (инкапсуляция): _brand, _model, _year, _price.
# ◦	Абстрактный метод calculate_tax(), который будет переопределен в наследниках.
# ◦	Метод vehicle_info(), возвращающий информацию о транспортном средстве.
# 2	Класс Car (наследник Vehicle):
# ◦	Реализация метода calculate_tax(): Налог рассчитывается как 10% от цены.
# 3	Класс Truck (наследник Vehicle):
# ◦	Перегрузка метода calculate_tax(weight=None):
# ▪	Если вес не указан, налог = 12% от цены.
# ▪	Если указан вес, налог увеличивается на 1% за каждые 1000 кг веса.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, year, price):
        self._brand = brand
        self._model = model
        self._year = year
        self._price = price

    @abstractmethod
    def calculate_tax(self):
        pass

    def vehicle_info(self):
        return self._brand, self._model, self._year, self._price

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def price(self):
        return self._price


class Car(Vehicle):
    def calculate_tax(self):
        return self._price * 0.1


class Truck(Vehicle):
    def calculate_tax(self, weight=None):
        if weight is None:
            return self._price * 0.12
        else:
            return self._price * (0.12 + (0.01 * (weight // 1000)))


# ТЕСТИРОВАНИЕ КОДА

# легковой автомобиль 1
car_1 = Car('mazda', 'CX-5', 2019, 2000000)
print(car_1.vehicle_info())
print(f"Налог на {car_1.brand}, {car_1.year} года выпуска = {car_1.calculate_tax()} рублей.")

# легковой автомобиль 2
car_2 = Car('BMW', 'X5', 2018, 4580000)
print(car_2.vehicle_info())
print(f"Налог на {car_2.brand}, {car_2.year} года выпуска = {car_2.calculate_tax()} рублей.")

# легковой автомобиль 3
car_3 = Car('ЗАЗ', '968', 1975, 2000)
print(car_3.vehicle_info())
print(f"Налог на {car_3.brand}, {car_3.year} года выпуска = {car_3.calculate_tax()} рублей.")

# грузовой автомобиль 1, вес не указан
truck_1 = Truck('VOLVO', 'FE', 2011, 1000000)
print(truck_1.vehicle_info())
print(f"Налог на {truck_1.brand}, {truck_1.year} года выпуска = {truck_1.calculate_tax()} рублей.")

# грузовой автомобиль 2, вес не указан
truck_2 = Truck('КамАЗ', 65117, 2024, 2000000)
print(truck_2.vehicle_info())
print(f"Налог на {truck_2.brand}, {truck_2.year} года выпуска = {truck_2.calculate_tax()} рублей.")

# грузовой автомобиль 3, вес 3500 кг
truck_3 = Truck('КамАЗ', 65117, 2024, 2000000)
print(truck_3.vehicle_info())
print(f"Налог на {truck_3.brand}, {truck_3.year} года выпуска = {truck_3.calculate_tax(3500)} рублей.")

# грузовой автомобиль 4, вес 7950 кг
truck_4 = Truck('МаЗ', '544028-570-031', 2024, 2000000)
print(truck_4.vehicle_info())
print(f"Налог на {truck_4.brand}, {truck_4.year} года выпуска = {truck_4.calculate_tax(7950)} рублей.")
