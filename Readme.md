# Contact Search System Using Data Structures

## Overview
This project implements a simple **Contact Management System** using fundamental data structures.  
It allows users to add contacts, search contacts using keywords or exact names, and display contacts in forward or backward order.

The goal is to demonstrate practical use of:

- Hash Tables
- Doubly Linked Lists
- String Matching Algorithms

---

## Data Structures Used

### Hash Table
The system uses a Python dictionary to implement a **:contentReference[oaicite:0]{index=0}**.

Purpose:
- Provide **fast lookup of contacts by name**
- Average time complexity: **O(1)**

Example:
```

contacts_table = {
"alice": Contact("Alice", "1234567890")
}

```

---

### Doubly Linked List
Contacts are also stored in a **:contentReference[oaicite:1]{index=1}**.

Each node contains:
- A contact object
- A pointer to the previous node
- A pointer to the next node

Structure:
```

prev <-> Node <-> next

```

Purpose:
- Allow **forward traversal**
- Allow **backward traversal**

---

### String Matching
Keyword searching uses the **:contentReference[oaicite:2]{index=2}**.

The algorithm checks if a substring exists within a contact's name.

Example:
```

Search keyword: "Al"
Matches:
Alice

```

---

## System Architecture

The system contains the following components:

### Contact Class
Stores contact information.

Attributes:
- `name`
- `phone`

Example:
```

Contact("Alice", "1234567890")

```

---

### Node Class
Represents a node in the doubly linked list.

Attributes:
- `contact`
- `prev`
- `next`

---

### DoublyLinkedList Class
Responsible for storing contacts in order.

Main functions:
- `add(contact)`
- `display_forward()`
- `display_backward()`

---

### ContactManager Class
Main controller of the system.

Responsibilities:
- Manage contacts
- Store contacts in both:
  - hash table
  - doubly linked list
- Perform search operations

Functions:
- `add_contact(name, phone)`
- `search_by_name(name)`
- `search_by_keyword(keyword)`

---

## System Operations

### 1. Add Contact
Adds a contact to:
- the doubly linked list
- the hash table

Steps:
1. Create a Contact object
2. Insert it into the linked list
3. Store it in the dictionary

---

### 2. Search by Keyword
Finds contacts whose names contain a substring.

Example:

Input:
```

keyword = "Al"

```

Output:
```

Alice - 1234567890

```

---

### 3. Search by Exact Name
Uses the hash table for fast lookup.

Example:
```

search_by_name("Alice")

```

Output:
```

Found: Alice - 1234567890

```

---

### 4. Display Contacts Forward
Traverses the doubly linked list from **head to tail**.

Example:
```

Alice - 1234567890
Bob - 0987654321

```

---

### 5. Display Contacts Backward
Traverses the doubly linked list from **tail to head**.

Example:
```

Bob - 0987654321
Alice - 1234567890

```

---

## Menu Interface

The program provides a simple text menu:

```

1. Add Contact
2. Search by Keyword
3. Search by Exact Name
4. View All (Forward)
5. View All (Backward)
6. Exit

```

---

## Example Execution

```

Enter option: 1
Name: Alice
Phone: 1234567890
Contact added.

Enter option: 2
Search keyword: Al
Match found: Alice - 1234567890

```

---

## Time Complexity

| Operation | Data Structure | Complexity |
|-----------|---------------|------------|
| Add Contact | Doubly Linked List | O(1) |
| Add Contact | Hash Table | O(1) |
| Search by Name | Hash Table | O(1) average |
| Search by Keyword | String Matching | O(n × m) |
| Display Contacts | Doubly Linked List | O(n) |

Where:
- **n** = number of contacts
- **m** = length of the keyword

---

## Advantages of This Design

- Fast lookup using a hash table
- Efficient traversal using a doubly linked list
- Simple substring search implementation
- Demonstrates multiple data structures working together

---

## Possible Improvements

Future enhancements could include:

- Implementing **:contentReference[oaicite:3]{index=3} for faster substring search
- Saving contacts to a file or database
- Adding contact deletion and editing
- Implementing a graphical user interface (GUI)

---

## Conclusion

This project demonstrates how different data structures can work together to solve a real-world problem.  
By combining hash tables, doubly linked lists, and string matching algorithms, the system provides efficient contact storage, retrieval, and search capabilities.
``
