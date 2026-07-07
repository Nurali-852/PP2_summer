import csv
from connection import connect

#1
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50),
                        phone VARCHAR(20)
                );
            """)
    print("Table created!")

#2
def from_csv():
    with connect() as conn:
        with conn.cursor() as cursor:
            with open("contacts.csv", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter = ";")

                for row in reader:
                    cursor.execute(
                        """
                        INSERT INTO phonebook(name, phone)
                        VALUES (%s, %s)
                        """,
                        (row[0], row[1])
                    )

    print("CSV contacts inserted")

#3
def add_number():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook(name, phone) VALUES(%s, %s)
            """,
            (name, phone)
            )
    print("New contact added!")

#4
def change_name():
    old_name = input("Old name: ")
    new_name = input("New name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET name = %s WHERE name = %s",
        (new_name, old_name)
    )

    conn.commit()
    print("Updated:", cur.rowcount)

    cur.close()
    conn.close()

def change_phone():
    name = input("Contact name: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    print("Updated:", cur.rowcount)

    cur.close()
    conn.close()

#5
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

def find_by_name():
    part = input("Enter name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name = %s", (part,))

    rows = cur.fetchall()

    if len(rows) == 0:
        print("Nothing found.")
    else:
        for row in rows:
            print(row)
    cur.close()
    conn.close()


def find_by_prefix():
    prefix = input("Enter phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE CAST(phone AS TEXT) LIKE %s ORDER BY id",
        (prefix + "%",)
    )
    print(cur.fetchall())

    cur.close()
    conn.close()

#6
def remove_by_name():
    name = input("Name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )
    conn.commit()
    print("Deleted:", cur.rowcount)
    cur.close()
    conn.close()

def remove_by_phone():
    phone = input("Phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )

    conn.commit()
    print("Deleted:", cur.rowcount)
    cur.close()
    conn.close()

def menu():
    while True:
        print("\nPhoneBook")
        print("1 - Add contact")
        print("2 - Import from csv")
        print("3 - Show all contacts")
        print("4 - Search by name")
        print("5 - Search by phone prefix")
        print("6 - Update name")
        print("7 - Update phone")
        print("8 - Delete by name")
        print("9 - Delete by phone")
        print("0 - Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_number()
        elif choice == "2":
            from_csv()
        elif choice == "3":
            show_all()
        elif choice == "4":
            find_by_name()
        elif choice == "5":
            find_by_prefix()
        elif choice == "6":
            change_name()
        elif choice == "7":
            change_phone()
        elif choice == "8":
            remove_by_name()
        elif choice == "9":
            remove_by_phone()
        elif choice == "0":
            print("Bye, bye!")
            break
        else:
            print("Wrong choice")

menu()