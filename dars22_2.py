import json
def write_json(d:dict):
    with open("contact.json","w") as f:
        json.dump(d, f, indent=4)
def read_json():
    try:
        with open("contact.json","r") as f:
            s=json.load(f)
            return s
    except:
        return {}
def view_contacts(data=None):
    if data is None:
        data = read_json()
    if not data:
        print("No contacts")
        return
    for k,v in data.items():
        print(f"id.{k}. name: {v['name']}, phone: {v['phone']}")
def add_contacts():
    data=read_json()
    name=input("Name: ")
    phone=input("Phone: ")
    s={
        phone:{
            "name": name,
            "phone": phone
        }
    }
    if data:
        data.update(s)
        write_json(data)
    else:
        write_json(s)
    print("Contact added")
def manage_contact():
    while True:
        kod = input(" 1. View contacts \n 2. Add contact \n 3. End the process \n ")
        if kod == "1":
            view_contacts()
        elif kod == "2":
            add_contacts()
        elif kod == "3":
            print("As you wish ...")
            break
        else:
            print("Invalid input")
            return
manage_contact()