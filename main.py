class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, contact):
        new_node = Node(contact)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            c = current.contact
            print(f"{c.name} - {c.phone}")
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            c = current.contact
            print(f"{c.name} - {c.phone}")
            current = current.prev


# Naive substring search
def substring_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i+m].lower() == pattern.lower():
            return True
    return False


class ContactManager:
    def __init__(self):
        self.contacts_list = DoublyLinkedList()
        self.contacts_table = {}  # Hash table

    def add_contact(self, name, phone):
        contact = Contact(name, phone)

        self.contacts_list.add(contact)
        self.contacts_table[name.lower()] = contact

        print("Contact added.")

    def search_by_name(self, name):
        contact = self.contacts_table.get(name.lower())

        if contact:
            print(f"Found: {contact.name} - {contact.phone}")
        else:
            print("Contact not found.")

    def search_by_keyword(self, keyword):
        current = self.contacts_list.head
        found = False

        while current:
            name = current.contact.name
            if substring_match(name, keyword):
                print(f"Match found: {name} - {current.contact.phone}")
                found = True
            current = current.next

        if not found:
            print("No matches found.")


def menu():
    manager = ContactManager()

    while True:
        print("\n1. Add Contact")
        print("2. Search by Keyword")
        print("3. Search by Exact Name")
        print("4. View All (Forward)")
        print("5. View All (Backward)")
        print("6. Exit")

        choice = input("\nEnter option: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            manager.add_contact(name, phone)

        elif choice == "2":
            keyword = input("Search keyword: ")
            manager.search_by_keyword(keyword)

        elif choice == "3":
            name = input("Enter exact name: ")
            manager.search_by_name(name)

        elif choice == "4":
            manager.contacts_list.display_forward()

        elif choice == "5":
            manager.contacts_list.display_backward()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option.")


menu()