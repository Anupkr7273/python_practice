class Car:
    total_car=0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1
    def full_name(self):
        return f"{self.__brand} {self.model}"    

    def chai_brand(self):
        return self.__brand +"!"
    def fuel_type(self):
        return "Petrol or Diesal"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric charge"
# my_car=Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car= Car("Tata","Safari")
# print(my_new_car.model)

# my_tesla=ElectricCar("Tesla","Model S","85kwh")
# # print(my_tesla.__brand)
# print(my_tesla.fuel_type())

Car("Tata","Safari")
Car("Tata","nexon")
print(Car.total_car)
 