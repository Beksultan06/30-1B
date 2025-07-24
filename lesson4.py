from abc import ABC, abstractmethod
import random


class Vehicle(ABC):
    total_vehicles = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._endgine_started = False
        Vehicle.total_vehicles += 1

    def start_engine(self):
        self._endgine_started = True
        print(f"{self.brand} {self.model} : Engine Start")

    def stop_engie(self):
        self._endgine_started = True
        print(f"{self.brand} {self.model} : Engine Stop")

    def __str__(self):
        return f"{self.brand} {self.model}"

    @abstractmethod
    def drive(self):
        pass

    @classmethod 
    def get_total_vihecles(cls):
        return cls.total_vehicles

    @staticmethod
    def vehicle_types():
        return ['Car', 'Truck', 'Bus', 'Motorcycle']


class Car(Vehicle):
    def drive(self):
        if self._endgine_started:
            print(f"{self} удут по дороге")
        else:
            print(f"{self} не может ехать двигатель не запущен")

class Truck(Vehicle):
    def __init__(self, brand, model, capacity_tons):
        super().__init__(brand, model)
        self.capacity_tons = capacity_tons

    def drive(self):
        if self._endgine_started:
            print(f"{self} везет {self.capacity_tons} тонн груз")
        else:
            print(f"{self} не может ехать двигатель не запущен")

    def __len__(self):
        return int(self.capacity_tons * 100)

class Motorcycle(Vehicle):
    def drive(self):
        if self._endgine_started:
            print(f"{self} мчится по трассе")
        else:
            print(f"{self} не может ехать двигатель не запущен")


class MusicSystem:
    def play_music(self):
        print("Музыка играет")

class Bus(Vehicle, MusicSystem):
    def __init__(self, brand, model, passengers):
        super().__init__(brand, model)
        self.passengers = passengers

    def drive(self):
        if self._endgine_started:
            print(f"{self} везет{self.passengers} пассажирова")
        else:
            print(f"{self} не может ехать двигатель не запущен")

    def __getitem__(self, index):
        return f"PAssengers #{index + 1}"

    def __len__(self):
        return self.passengers


def main():
    car = Car("Toyotsa", 'corolla')
    truck = Truck("Volvo", 'FH16', 25)
    moto = Motorcycle("Yamaha", 'QEW-T3')
    bus = Bus("Mersedes", ' Sprinter', 19)

    car.start_engine()
    truck.start_engine()
    bus.start_engine()

    for vehicle in [car, truck, moto, bus]:
        vehicle.drive()
        
    print(car._endgine_started)

    def go_all(vehicles):
        for v in vehicles:
            v.drive()

    go_all([car, truck, moto, bus])

    print(f"Вместимость грузовика {len(truck)} kg")
    print(f"Пассадиров в автобусе {len(bus)}")
    print(f"Кто сижди на месте 3 {bus[2]}")

    print(f"Всего транспорта {Vehicle.get_total_vihecles()}")
    print(f"Типы трансорта {Vehicle.vehicle_types()}")

    bus.play_music()

main()