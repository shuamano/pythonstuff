class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return(long_name.title())
    
    def get_odometer_reading(self):
        print(f"this {my_car.get_descriptive_name()} has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
       if mileage >= self.odometer:
            self.odometer = mileage  
       else:
        print("you cant roll back miles dumbass")

    def increment_odometer(self, increment):
        self.odometer += increment

my_car = Car('Honda', 'odyssey', 2006)

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() 

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size} Kwh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 250
        
        print(f"This car can go about {range} miles on a charge.")
    

my_tesla = ElectricCar('tesla', 'model x', '2017')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()