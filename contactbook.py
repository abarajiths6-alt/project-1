class ContactManager:
    def __init__(self):
        self.contacts = []

    # Add Contact
    def add_contact(self):
        contact = {
            "Name": input("Enter Name: "),
            "Phone": input("Enter Phone: "),
            "Email": input("Enter Email: "),
            "Address": input("Enter Address: ")
        }

        self.contacts.append(contact)
        print("✅ Contact Added Successfully!")

    # View Contacts
    def view_contacts(self):
        if not self.contacts:
            print("No Contacts Available.")
            return

        print("\n------ CONTACT LIST ------")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact['Name']} - {contact['Phone']}")

    # Search Contact
    def search_contact(self):
        key = input("Enter Name or Phone: ").lower()

        for contact in self.contacts:
            if key == contact["Name"].lower() or key == contact["Phone"]:
                print("\nContact Found")
                for k, v in contact.items():
                    print(f"{k}: {v}")
                return

        print("❌ Contact Not Found.")

    # Update Contact
    def update_contact(self):
        name = input("Enter Contact Name to Update: ").lower()

        for contact in self.contacts:
            if contact["Name"].lower() == name:
                contact["Phone"] = input("New Phone: ")
                contact["Email"] = input("New Email: ")
                contact["Address"] = input("New Address: ")
                print("✅ Contact Updated Successfully!")
                return

        print("❌ Contact Not Found.")

    # Delete Contact
    def delete_contact(self):
        name = input("Enter Contact Name to Delete: ").lower()

        for contact in self.contacts:
            if contact["Name"].lower() == name:
                self.contacts.remove(contact)
                print("✅ Contact Deleted Successfully!")
                return

        print("❌ Contact Not Found.")

    # Menu
    def menu(self):
        while True:
            print("\n========== CONTACT MANAGEMENT ==========")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()

            elif choice == "2":
                self.view_contacts()

            elif choice == "3":
                self.search_contact()

            elif choice == "4":
                self.update_contact()

            elif choice == "5":
                self.delete_contact()

            elif choice == "6":
                print("Thank You for Using Contact Manager!")
                break

            else:
                print("❌ Invalid Choice!")


# Main Program
if __name__ == "__main__":
    app = ContactManager()
    app.menu()