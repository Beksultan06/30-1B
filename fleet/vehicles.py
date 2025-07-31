from abc import ABC, abstractmethod

class Vihicle(ABC):
    _vehicle_count = 0

    def __init__(self, brand : str, model : str, year : int):
        self.brand = brand
        self.model = model
        self.year = year
        Vihicle._vehicle_count += 1

    @abstractmethod
    def get_info(self):
        pass

    @classmethod
    def total_vehicles(cls):
        return cls._vehicle_count

    @property
    def full_name(self):
        return f"{self.brand} {self.model} {self.year}"