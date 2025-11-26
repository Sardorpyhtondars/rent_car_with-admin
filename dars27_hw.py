class Drivers:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.d_busy = False
        self.car_number = None

class Cars:
    def __init__(self, number, model):
        self.number = number
        self.model = model
        self.c_busy = False

class Rent:
    def __init__(self, driver, car):
        self.driver = driver
        self.car = car

class System:
    def __init__(self, drivers, cars):
        self.drivers = drivers
        self.cars = cars
        self.rents = []

    def add_car(self):
        car_number=input( "Enter car number:\n ")
        car_model=input( "Enter car model:\n ")
        car=Cars(car_number,car_model)
        self.cars.append(car)

    def add_driver(self):
        driver_name=input( "Enter driver name:\n ")
        driver_surname=input( "Enter driver surname:\n ")
        driver_age=input( "Enter driver age:\n ")
        driver=Drivers(driver_name,driver_surname,driver_age)
        self.drivers.append(driver)

    def free_drivers(self):
        print(" Free drivers:\n")
        for driver in self.drivers:
            if not driver.d_busy:
                print(f" Name: {driver.name}, Surname: {driver.surname}, Age: {driver.age}\n")

    def busy_drivers(self):
        print(" Busy drivers:")
        for driver in self.drivers:
            if driver.d_busy:
                print(f" Name: {driver.name}, Surname: {driver.surname}, Age: {driver.age}\n")

    def free_cars(self):
        print(" Free cars:\n")
        for car in self.cars:
            if not car.c_busy:
                print(f" Car number: {car.number}, Car model: {car.model}\n")

    def rented_cars(self):
        print(" Rented cars:\n")
        for car in self.cars:
            if car.c_busy:
                print(f" Car number: {car.number}, Card model: {car.model}\n")

    def rent_car(self):
        print(" Choose a driver:\n")
        count=0
        free_drivers=[]
        for driver in self.drivers:
            if not driver.d_busy:
                count=count+1
                print(f" {count}. Name: {driver.name}, Surname: {driver.surname}, Age: {driver.age}\n")
                free_drivers.append(driver)
        if len(free_drivers)==0:
            print(" No free drivers\n")
            return
        d_index=int(input( "Enter driver number:\n "))
        driver=free_drivers[d_index-1]

        print(" Choose a car:\n")
        count=0
        free_cars=[]
        for car in self.cars:
            if not car.c_busy:
                count+=1
                print(f" {count}. Number: {car.number}, Model: {car.model}\n")
                free_cars.append(car)
        if len(free_cars)==0:
            print(" No free cars\n")
            return
        c_index=int(input( "Enter car number:\n "))
        car=free_cars[c_index-1]

        driver.d_busy=True
        driver.car_number=car.number
        car.c_busy=True
        self.rents.append(Rent(driver, car))
        print(" Car successfully rented\n")

    def cancel_rent(self):
        print(" Choose a driver:\n")
        count=0
        busy_drivers=[]
        for driver in self.drivers:
            if driver.d_busy:
                count+=1
                print(f" {count}. Name: {driver.name}, Surname: {driver.surname}, Age: {driver.age}, Renting car: {driver.car_number}\n")
                busy_drivers.append(driver)
        if len(busy_drivers)==0:
            print(" No busy drivers\n")
            return
        index=int(input(" Enter driver number:\n "))
        driver=busy_drivers[index-1]
        for r in self.rents:
            if r.driver==driver:
                self.rents.remove(r)
                break

        car=None
        for c in self.cars:
            if c.number==driver.car_number:
                car=c
                break

        driver.d_busy=False
        driver.car_number=None
        car.c_busy=False

d1 = Drivers("Alisher", "Toxirov", "27")
d2 = Drivers("Alexander", "Ikromov", "28")
d3 = Drivers("Tohir", "Komilov", "39")

c1=Cars("A111AA", "Malibu")
c2=Cars("B191BC", "Nexia 3")
c3=Cars("M498CB", "Gentra")

system = System([],[])

system.drivers.append(d1)
system.drivers.append(d2)
system.drivers.append(d3)

system.cars.append(c1)
system.cars.append(c2)
system.cars.append(c3)

while True:
    kod=input(" 1. Show free drivers\n 2. Show busy drivers\n 3. Show free cars\n 4. Show busy cars\n 5. Rent a car\n 6. Cancel rent\n 7. Add driver\n 8. Add car\n 9. Exit\n ").strip()

    if kod == "1":
        system.free_drivers()
    elif kod == "2":
        system.busy_drivers()
    elif kod == "3":
        system.free_cars()
    elif kod == "4":
        system.rented_cars()
    elif kod == "5":
        system.rent_car()
    elif kod == "6":
        system.cancel_rent()
    elif kod == "7":
        system.add_driver()
    elif kod == "8":
        system.add_car()
    elif kod == "9":
        break
    else:
        print("Invalid input")
        continue
