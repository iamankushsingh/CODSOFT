import sqlite3

# Database Setup
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE,
                    email TEXT,
                    address TEXT)''')
conn.commit()

# Function to Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    address = input("Enter Address (optional): ")

    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", 
                       (name, phone, email, address))
        conn.commit()
        print("Contact Added Successfully!")
    except sqlite3.IntegrityError:
        print("Error: Contact with this phone number already exists.")

# Function to View All Contacts
def view_contacts():
    cursor.execute("SELECT name, phone FROM contacts")
    contacts = cursor.fetchall()

    if not contacts:
        print("No contacts found!")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts:
            print(f"{name} - {phone}")

# Function to Search Contact
def search_contact():
    search_query = input("Enter Name or Phone Number to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
                   (f"%{search_query}%", f"%{search_query}%"))
    results = cursor.fetchall()

    if results:
        for contact in results:
            print(f"\nID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")
    else:
        print("No contact found!")

# Function to Update Contact
def update_contact():
    phone = input("Enter the Phone Number of the contact to update: ")
    cursor.execute("SELECT * FROM contacts WHERE phone=?", (phone,))
    result = cursor.fetchone()

    if result:
        new_name = input(f"Enter new name (Leave blank to keep {result[1]}): ") or result[1]
        new_email = input(f"Enter new email (Leave blank to keep {result[3]}): ") or result[3]
        new_address = input(f"Enter new address (Leave blank to keep {result[4]}): ") or result[4]

        cursor.execute("UPDATE contacts SET name=?, email=?, address=? WHERE phone=?", 
                       (new_name, new_email, new_address, phone))
        conn.commit()
        print("Contact Updated Successfully!")
    else:
        print("Contact not found!")

# Function to Delete Contact
def delete_contact():
    phone = input("Enter the Phone Number of the contact to delete: ")
    cursor.execute("DELETE FROM contacts WHERE phone=?", (phone,))
    
    if cursor.rowcount > 0:
        conn.commit()
        print("Contact Deleted Successfully!")
    else:
        print("Contact not found!")

# Main Menu
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
    conn.close()
