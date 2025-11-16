import re
n=r"^[A-Za-zА-Яа-яЎўҚқҒғҲҳЁё\s]+$"
p=r"^\+998\d{9}$"
e=r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

Contact1=Contact('Shoxrux', '+998900000000', 'shox@gmail.com')
Contact2=Contact('Bobur', '+998999999999', 'bob@gmail.com')
Contact3=Contact('Alisher', '+998977777777', 'ali@gmail.com')

base=[Contact1,Contact2,Contact3]

def view_contacts(s:list):
    count=0
    for item in s:
        count+=1
        print(f"{count}. {item.name} {item.phone} {item.email}")
# view_contacts(base)
def add_contact(s:list):
    contact_name=input("Enter contact name:\n")
    if not re.match(n,contact_name):
        print("Invalid name format")
        return
    contact_phone=input("Enter contact phone:\n")
    if not re.match(p,contact_phone):
        print("Invalid phone format")
        return
    contact_email=input("Enter contact email:\n")
    if not re.match(e,contact_email):
        print("Invalid email format")
        return
    contact=Contact(contact_name, contact_phone, contact_email)
    s.append(contact)
    view_contacts(s)
# add_contact(base)
def update_contact(s:list):
    view_contacts(s)
    number=input("Enter contact number of the person to update:\n")
    contact_=None
    for i in s:
        if i.phone==number:
            contact_=i
            break
    if contact_ is None:
        print("Contact not found")
        return
    change=input("What do you want to change?\n1.name\n2.phone number\n3.email\n").strip()
    if change=="1":
        new_name=input("Enter new contact name:\n")
        if new_name in [c.name for c in s]:
            print("Contact name already exists")
            return
        if not re.match(n,new_name):
            print("Contact name must not contain symbols and numbers")
            return
        contact_.name=new_name
        print("Contact name updated")
        return
    elif change=="2":
        new_phone=input("Enter new contact phone:\n")
        if new_phone in [c.phone for c in s]:
            print("Contact phone number already exists")
            return
        if not re.match(p,new_phone):
            print("Contact phone number is incorrect")
            return
        contact_.phone=new_phone
        print("Contact phone updated")
        return
    elif change=="3":
        new_email=input("Enter new contact email:\n")
        if new_email in [c.email for c in s]:
            print("Contact email already exists")
            return
        if not re.match(e,new_email):
            print("Contact email is incorrect")
            return
        contact_.email=new_email
        print("Contact email updated")
        return
    else:
        print("Invalid input")
        return
# update_contact(base)
def delete_contact(s:list):
    view_contacts(s)
    number=input("Enter contact number of the person to delete:\n")
    if not re.match(n,number):
        print("Invalid phone number")
        return
    contact=None
    for i in s:
        if i.phone==number:
            contact=i
            break
    if contact is None:
        print("Contact not found")
        return
    s.remove(contact)
    print("Contact deleted")
    view_contacts(s)
# delete_contact(base)
def contact_manager():
    while True:
        kod=input(" 1. View all contacts\n 2. Add contact\n 3. Update contact\n 4. Delete contact\n").strip()
        if kod=="1":
            view_contacts(base)
        elif kod=="2":
            add_contact(base)
        elif kod=="3":
            update_contact(base)
        elif kod=="4":
            delete_contact(base)
        else:
            print("Invalid input")
            continue
contact_manager()