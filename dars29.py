class User:
    def __init__(self, username, phone, seria, password, age):
        self.username = username
        self.phone = phone
        self.seria = seria
        self.password=password
        self.age = age
        self.is_active = True
        self.is_admin = False

    def update_info(self):
        print(f"Updating information for {self.username}")
        while True:
            kod = input(
                "What do you want to update?\n 1. Name \n 2. Phone \n 3. Serial number \n 4. Password \n 5. Age \n 6. Exit \n ")
            if kod == "1":
                self.username = input("Enter your name: ")
            elif kod == "2":
                self.phone = input("Enter your phone number: ")
            elif kod == "3":
                self.seria = input("Enter your serial number: ")
            elif kod == "4":
                self.password = input("Enter your password: ")
            elif kod == "5":
                self.age = input("Enter your age: ")
            elif kod == "6":
                break
            else:
                print("Invalid input")
                continue
        print("Information updated")

class Car:
    def __init__(self, model, brand, year, seria, ):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True
class Order:
    def __init__(self,user_id,car_id,date_start,date_end):
        self.user_id =user_id
        self.car_id =car_id
        self.date_start =date_start
        self.date_end =date_end
        self.is_active = True

class Park:
    def __init__(self,title):
        self.title =title
        self.users  =[]
        self.cars  =[]
        self.orders  =[]

    def edit_user_info(self,user):
        if user.is_admin:
            print("All users:\n")
            count=0
            for user in self.users:
                count+=1
                print(f" {count}. {user.username}\n")
            kod=int(input("Select user number:\n "))
            if 1<=kod<=len(self.users):
                self.users[kod-1].update_info()
        else:
            user.update_info()

    def authenticate(self):
        username=input(" Enter your username:\n ")
        for user in self.users:
            if user.username == username:
                password=input(" Enter your password:\n ")
                if password == user.password:
                    print(f" Welcome {user.username}")
                    return user
        return False

park=Park("Park")
admin=User("Admin","123","2020","0000", 23)
admin.is_admin = True
park.users.append(admin)

driver=User("Driver","456","1010","1111", 32)
driver.is_admin = False
park.users.append(driver)
def admin_manager(park,user):
    while True:
        kod=input(" 1. Edit user info\n 2. View all users\n 3. Add car\n 4. View all cars\n 5. Exit\n ")
        if kod == "1":
            park.edit_user_info(user)
        elif kod == "2":
            print("All users:\n")
            count=0
            for user in park.users:
                count+=1
                print(f" {count}. {user.username}, {user.phone}, {user.seria}, {user.age}")
        elif kod == "3":
            model=input("Enter your model:\n ")
            brand=input("Enter your brand:\n ")
            year=input("Enter your year:\n ")
            seria=input("Enter your serial number:\n ")
            car=Car(model,brand,year,seria)
            park.cars.append(car)
            print("Car added.")
        elif kod == "4":
            print("All cars:\n")
            count=0
            for car in park.cars:
                count+=1
                print(f" {count}. {car.model}, {car.brand}, {car.year}, {car.seria}")
        elif kod == "5":
            break
        else:
            print("Invalid input")
            continue

def driver_manager(park,user):
    while True:
        kod=input(" 1. Edit my info\n 2. Exit\n ")
        if kod == "1":
            park.edit_user_info(user)
        elif kod == "2":
            break
        else:
            print("Invalid input")
            continue

def park_manager(p:Park):
    user=p.authenticate()
    if user.is_admin:
        print("\n Welcome admin\n ")
        admin_manager(p,user)
    else:
        print("\n Welcome user\n ")
        driver_manager(p,user)
park_manager(park)