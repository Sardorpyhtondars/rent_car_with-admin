import csv
import re
import os
p= r"^\+998\d{9}$"
def add_contact_csv():
    name=input("Enter name: ").strip()
    while True:
        phone=input("Enter phone number: ")
        if re.match(p,phone):
            break
        print("Phone number is not valid. Please try again.\n")
    a=os.path.exists("contact.csv")
    with open('contact.csv', 'a', newline='', encoding="utf-8") as f:
        writer=csv.writer(f)
        if not a:
            writer.writerow(["name","phone"])
        writer.writerow([name,phone])
    print("Contact has been saved successfully.")
# add_contact_csv()
def view_contact_csv():
    try:
        with open('contact.csv', 'r') as f:
            reader = csv.reader(f)
            row=list(reader)
    except:
        print("You have no contacts.")
        return
    count=0
    for i in row:
        if count!=0:
            print(f"{count} {i[0]} {i[1]}")
        else:
            print(f"   {i[0]} {i[1]}")
        count+=1
# view_contact_csv()
def update_contact_csv():
    with open('contact.csv', 'r') as f:
        reader = csv.reader(f)
        row=list(reader)
        contact_id=int(input("Enter contact id:\n"))
        contact_change=int(input("What do you want to change:\n"))+1
        new_contact=input("Enter new contact information:\n").strip()
        row[contact_id][contact_change]=new_contact
    with open('contact.csv', 'w', newline='', encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows(row)
        print("Contact has been updated successfully.")
# update_contact_csv()
def delete_contact_csv():
    with open('contact.csv', 'r') as f:
        reader = csv.reader(f)
        row=list(reader)
        contact_id=int(input("Enter contact id that you want to remove:\n"))
        row.pop(contact_id)
    with open('contact.csv', 'w', newline='', encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows(row)
        print("Contact has been deleted successfully.")
# delete_contact_csv()
def contact_manager_csv():
    while True:
        kod=input(" 1. View contacts\n 2. Add contact\n 3. Delete contact\n 4. Update contact\n 5. Return home\n").strip()
        if kod=="1":
            view_contact_csv()
            print()
        elif kod=="2":
            add_contact_csv()
            print()
        elif kod=="3":
            delete_contact_csv()
            print()
        elif kod=="4":
            update_contact_csv()
            print()
        elif kod=="5":
            break
        else:
            print("Wrong input. Please try again.\n")
# contact_manager_csv()
def view_message_csv():
    try:
        with open('message.csv', 'r') as f:
            reader = csv.reader(f)
            row=list(reader)
    except:
        print("You have no messages.")
        return
    count=0
    for i in row:
        if count!=0:
            print(f"{count} {i[0]} {i[1]} {i[2]}")
        else:
            print(f"   {i[0]} {i[1]} {i[2]}")
        count+=1
# view_message_csv()
def send_message_csv():
    with open("contact.csv", "r") as f:
        reader = csv.reader(f)
        contacts=list(reader)[1:]
    contact_found=None
    while not contact_found:
        contact_number=input("Enter contact number:\n").strip()
        for i in contacts:
            if i[1]==contact_number:
                contact_found=i
                break
        if not contact_found:
            print("Contact not found")
    whom=contact_found[0]
    message=input("Enter message:\n ").strip()
    file_exists=os.path.exists("message.csv")
    with open('message.csv', 'a', newline='', encoding="utf-8") as f:
        writer=csv.writer(f)
        if not file_exists:
            writer.writerow(["whom", "phone", "message"])
        writer.writerow([whom, contact_number, message])
    print("Message has been sent successfully.")
# send_message_csv()
def delete_message_csv():
    with open("message.csv", "r") as f:
        reader = csv.reader(f)
        row=list(reader)
        message_id = int(input("Enter message id that you want to remove:\n"))
        row.pop(message_id)
    with open('message.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(row)
        print("Message has been deleted successfully.")
# delete_message_csv()
def message_manager_csv():
    while True:
        kod=input(" 1. View messages\n 2. Send message\n 3. Delete message\n 4. Return home\n").strip()
        if kod=="1":
            view_message_csv()
            print()
        elif kod=="2":
            send_message_csv()
            print()
        elif kod=="3":
            delete_message_csv()
            print()
        elif kod=="4":
            break
        else:
            print("Wrong input. Please try again.\n")
            return
# message_manager_csv()
def head_manager_csv():
    while True:
        kod=input(" 1. Contact settings\n 2. Message settings\n 3. Close\n")
        if kod=="1":
            contact_manager_csv()
            print()
        elif kod=="2":
            message_manager_csv()
            print()
        elif kod=="3":
            return
        else:
            print("Wrong input. Please try again.\n")
head_manager_csv()