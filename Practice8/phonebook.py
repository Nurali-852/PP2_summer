import re
from connection import connect

#1
def find_by_pattern():
    patt = input("Enter pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s::text)", (patt,))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("Nothing found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()

#2
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s::text, %s::text)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added or updated.")

#3
def add_many_contacts():
    names = []
    phones = []
    bad = []

    count = int(input("How many contacts do you want to add? "))

    for i in range(count):
        print(f"\nContact {i + 1}")
        nm = input("Name: ")
        ph = input("Phone: ")

        if re.match(r'^\+?[0-9]{5,15}$', ph):
            names.append(nm)
            phones.append(ph)
        else:
            bad.append((nm, ph))

    if bad:
        print("\nIncorrect data (not added):")
    for nm, ph in bad:
        print(nm, ph)

    if names:
        conn = connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "CALL insert_many_contacts(%s, %s)",
                (names, phones)
            )
            conn.commit()
            print("Added new contacts")
        except Exception as e:
            conn.rollback()
            print("Error")
        finally:
            cur.close()
            conn.close()

    print("Contacts import finished.")

#4
def show_paginated():
    lim = int(input("Enter limit: "))
    offs = int(input("Enter offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s::int, %s::int)",
        (lim, offs)
    )
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No contacts.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()

#5
def remove_contact():
    val = input("Enter name or phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s::text)", (val,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted.")

def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No contacts.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()

def menu():
        while True:
            print("\nPhoneBook")
            print("1 - Add or update contact")
            print("2 - Add many contacts")
            print("3 - Show all contacts")
            print("4 - Search by pattern")
            print("5 - Show paginated contacts")
            print("6 - Delete by name or phone")
            print("0 - Exit")

            choice = input("Choose: ")

            if choice == "1":
                add_contact()
            elif choice == "2":
                add_many_contacts()
            elif choice == "3":
                show_all()
            elif choice == "4":
                find_by_pattern()
            elif choice == "5":
                show_paginated()
            elif choice == "6":
                remove_contact()
            elif choice == "0":
                print("Bye, bye!")
                break
            else:
                print("Wrong choice")
                
menu()