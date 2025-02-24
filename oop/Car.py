class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def set_brand(self):pass
        

    def get_brand(self): #getter
        return self.__brand
    
    def ride(self):
        print("riding")
    def get_car_details(self):
        return f"brand: {self.__brand} model: {self.model}"


car=Car("audi","w1")
print(car.getCarDetails())
car.ride()


#- Inheritance
class ElectircCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


tesla=ElectircCar("Tesla","T1","5000kwh")
print(tesla.getCarDetails())
tesla.ride()

#-Encapsulation
        