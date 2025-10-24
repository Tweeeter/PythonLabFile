# Create a class (Encapsulation)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Car: {self.brand} {self.model}")

# Create objects (Inheritance)
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
    
    def display(self):
        print(f"Electric Car: {self.brand} {self.model}, Battery: {self.battery}kWh")

# Create objects
car1 = Car("Toyota", "Camry")
car2 = ElectricCar("Tesla", "Model 3", 75)

# Display (Polymorphism)
car1.display()
car2.display()
