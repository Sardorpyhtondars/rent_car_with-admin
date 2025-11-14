students={
    "+998900000000": {
        "name":"Asad",
        "age":22,
        "phone":"+998900000000",
        "email":"abcs@gmail.com",
    },
    "+998777777777": {
        "name":"Sherzod",
        "age":20,
        "phone":"+998777777777",
        "email":"xyz123@mail.ru",
    }
}
import re
p= r"^\+998\d{9}$"
e= r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

def addstudents(d:dict):
    name=input("Enter your name:")
    age=input("Enter your age:")
    while True:
        phone=input("Enter your phone:")
        if re.match(p,phone):
            break
        print("Your phone number is not valid. Please try again.\n")
    while True:
        email=input("Enter your email:").strip()
        if re.match(e,email):
            break
        print("Your email is not valid. Please try again.\n")
    s={
        phone: {
            "name":name,
            "age":age,
            "phone":phone,
            "email":email,
        }
    }
    d.update(s)
def viewstudents(d:dict):
    for k,v in d.items():
        print(f" id.{k}. name={v['name']} age={v['age']} phone={v['phone']} email={v['email']}")
def managestudents(d:dict):
    while True:
        kod=input(" 1. View all students \n 2. Add student \n 3. End the process \n ")
        if kod == "1":
            viewstudents(d)
        elif kod == "2":
            addstudents(d)
        elif kod == "3":
            return
managestudents(students)