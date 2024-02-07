import car

my_electric_car = car.ElectricCar('Chevy', 'bolt', '2019')
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

my_rally_car = car.Car('Subaru', 'WRX', '2005')
print(my_rally_car.get_descriptive_name())
my_rally_car.get_odometer_reading()
