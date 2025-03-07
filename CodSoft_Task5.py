class Contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

    def update(self,name=None,phone=None,email=None,address=None):
        if name:
            self.name=name
        if phone:
            self.phone=phone
        if email:
            self.email=email
        if address:
            self.address=address

    def __str__(self):
        return f"Name:{self.name},Phone:{self.phone},Email:{self.email},Address:{self.address}"

class ContactBook:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,name,phone,email,address):
        for contact in self.contacts:
            if contact.phone==phone:
                print("Error:Phone number already exists!")
                return
        self.contacts.append(Contact(name,phone,email,address))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
            return
        for idx,contact in enumerate(self.contacts,start=1):
            print(f"{idx}.{contact}")

    def search_contact(self,query):
        results=[contact for contact in self.contacts if query in contact.name or query in contact.phone]
        if results:
            for contact in results:
                print(contact)
            else:
                print("No matching contacts found!")

    def update_contact(self,phone):
        for contact in self.contacts:
            if contact.phone==phone:
                print("Enter new deatils(press Enter to skip updating a field):")
                name=input(f"New name({contact.name}):")or contact.name
                email=input(f"New email({contact.email}):")or contact.email
                address=input(f"New address({contact.address}):")or contact.address
                contact.update(name=name,email=email,address=address)
                print("Contact updated succssfully")
                return
            print("Contact not found!")

    def delete_contact(self,phone):
        for contact in self.contacts:
            if contact.phone==phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
            print("Contact not found!")

def main():
        contact_book=ContactBook()

        while True:
            print("\n Contact Book Menu:")
            print("1.Add Contact")
            print("2.View Contacts")
            print("3.Search Contact")
            print("4.Update Contact")
            print("5.Delete Contact")
            print("6.Exit")

            choice=input("Choose an option:")

            if choice=="1":
                name=input("Enter Name:")
                phone=input("Enter Phone:")
                email=input("Enter Email:")
                address=input("Enter address:")
                contact_book.add_contact(name,phone,email,address)

            elif choice=="2":
                contact_book.view_contacts()

            elif choice=="3":
                query=input("Enter name or phone to search:")
                contact_book.search_contact(query)

            elif choice=="4":
                phone=input("Enter phone number of the contact to update:")
                contact_book.update_contact(phone)

            elif choice=="5":
                phone=input("Enter phone number of the contact to delete:")
                contact_book.delete_contact(phone)

            elif choice=="6": 
                print("Exiting Contact Book.Goodbye!")
                break

            else:
                print("Invalid choice,please try again!")

if __name__=="__main__":
    main()                          