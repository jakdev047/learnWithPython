"""
3. Data Structures
    Lists
    Tuples
    Sets
    Dictionaries
    Indexing & Slicing
    Adding, Updating & Removing Items
    Sorting & Searching
    Iterating Through Data Structures
    Nested Lists & Dictionaries
    Dictionary & Set Comprehensions
"""

"""
Data Structure              Ordered        Mutable    Duplicates
List []                     Yes            Yes        Allowed
Tuple ()                    Yes            No         Allowed
Set {}	                    No             Yes        Not allowed
Dictionary {key: value}   Insertion order  Yes        Keys unique

"""

# 1. Lists
list = [1, 2, 3, 4, 5]

print("\nList: ",list) # Output: [1, 2, 3, 4, 5]

list.append(6) # add element at the end of the list
print("\nlist.append(6): ",list) # Output: [1, 2, 3, 4, 5, 6]

list.remove(3) # remove element from the list
print("\nlist.remove(3): ",list) # Output: [1, 2, 4, 5, 6]

list.pop() # remove element from the end of the list
print("\nlist.pop(): ",list) # Output: [1, 2, 4, 5]

list.insert(2, 3) # insert element at the specific index  insert(index, element)
print("\nlist.insert(2, 3): ",list) # Output: [1, 2, 3, 4, 5]

list.reverse() # reverse the list
print("\nlist.reverse(): ",list) # Output: [5, 4, 3, 2, 1]

list.sort() # sort the list
print("\nlist.sort(): ",list) # Output: [1, 2, 3, 4, 5]

# 2. Tuples
tuple = (1, 2, 3, 4, 5)
print("\nTuple: ",tuple) # Output: [1, 2, 3, 4, 5]

tuple.count(2) # count the number of elements in the tuple
print("\ntuple.count(2): ",tuple) # Output: [1, 2, 3, 4, 5]

tuple.index(2) # find the index of the element in the tuple
print("\ntuple.index(2): ",tuple) # Output: [1, 2, 3, 4, 5]

person = ("Jubayer", 6, "Product Designer")

name, experience, profession = person

print(f"My name is {name}, I have {experience} years of experience and I am a {profession}") 
# Output: My name is Jubayer, I have 6 years of experience and I am a Product Designer

# 3. Set
set = {1, 2, 3, 4, 5}
print("\nSet: ",set) # Output: [1, 2, 3, 4, 5]

# Remove duplicate from List
numbers = [0, 20, 20, 30, 30, 40]

# unique_numbers = set(numbers)

# print(sorted(unique_numbers)) # [10, 20, 30, 40]

# Set operation
a = {1, 2, 3}
b = {3, 4, 5}

print("\na | b: ", a | b)  # Union [Result: {1, 2, 3, 4, 5}]
print("\na & b: ", a & b)  # Intersection [Result: {3}]
print("\na - b: ", a - b)  # Difference [Result: {1, 2}]


# 4. Dictionary
dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

print("Dictionary: ",dictionary) # Output: {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

student = {
    "name": "Jubayer Alam Khan",
    "subjects": {
        "English": 85,
        "math": 90,
        "chemistry": 88
    }
}

# Access Values
print("\nName: ",student["name"]) # Name:  Jubayer Alam Khan
print("\nEnglish: ",student["subjects"]["English"]) # English:  85

# get() Method
student = {
    "name": "Rahim",
    "marks": 85
}

print("\nget('marks'): ", student.get("marks")) # Output: 85
print("\nget('name'): ", student.get("name")) # Output: Rahim

# 5. Indexing & Slicing
numbers = [10, 20, 30, 40, 50]

# Example 01: Indexing
print("\nnumbers[0]: ", numbers[0]) # Output: 10
print("\nnumbers[-1]: ", numbers[-1]) # Output: 50

# Example 01: Slicing  list[start:stop:step]
print("\nnumbers[1:4]: ", numbers[1:4]) # Output: [20, 30, 40]
print("\nnumbers[:3]: ", numbers[:3]) # Output: [10, 20, 30]
print("\nnumbers[2:]: ", numbers[2:]) # Output: [30, 40, 50]
print("\nnumbers[::-1]: ", numbers[::-1]) # Output: [50, 40, 30, 20, 10]


# 6. Adding, Updating & Removing Items
fruits = ["Apple", "Banana"]

fruits.append("Mango") # add element at the end of the list -> Output: [Apple, Banana, Mango]
fruits.insert(1, "Orange") # insert element at the specific index -> Output: [Apple, Orange, Banana, Mango]
fruits[0] = "Guava" # update element at the specific index -> Output: [Guava, Orange, Banana, Mango]

print("\nadd, update & remove items: ",fruits) # Output: ['Guava', 'Orange', 'Banana', 'Mango']

fruits.remove("Banana") # remove element from the list -> Output: [Guava, Orange, Mango]
fruits.pop() # remove element from the end of the list -> Output: [Guava, Orange]
fruits.pop(1) # remove element at the specific index -> Output: [Guava]

print("\nremove: ",fruits) # Output: ['Guava']

# Set add & remove
skills = {"Python", "SQL"}

print("\nSet add & remove: ",skills) # Output: {'Python', 'SQL'}

skills.add("Machine Learning") # add element at the end of the set -> Output: {'Python', 'SQL', 'Machine Learning'}
skills.discard("SQL") # remove element from the set -> Output: {'Python', 'Machine Learning'}

print("\nSet add & remove: ",skills) # Output: {'Python', 'Machine Learning'}

# 7. Sorting & Searching

# sort() method - Sorts the list in ascending order
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("\nsort() method - Sorts the list in ascending order: ",numbers) # Output: [10, 20, 30, 40, 50]


# Decending order
numbers.sort(reverse=True)

print("\nDecending order: ",numbers) # Output: [50, 40, 30, 20, 10]


# sorted() function - Returns a new sorted list
numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers)

print("\nsorted() function - Returns a new sorted list: ",sorted_numbers) # Output: [10, 20, 30, 40, 50]

# Searching a value in a List
skills = ["Python", "SQL", "Pandas"]

if "Python" in skills:
    print("\nPython Found") 

print("\nIndex of SQL: ",skills.index("SQL")) # Output: 1

# Count occurrences
numbers = [1, 2, 3, 4, 2, 2, 5]

print("\nCount of 2: ",numbers.count(2)) # Output: 3

# 9. Iterating Through Data Structures

# List iteration
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(f"\nList iteration: {fruit}") # Output: Apple, Banana, Mango

# Tuple iteration
tuple = (1, 2, 3, 4, 5)

for number in tuple:
    print(f"\nTuple iteration: {number}") # Output: 1, 2, 3, 4, 5

# Set iteration
set = {1, 2, 3, 4, 5}

for number in set:
    print(f"\nSet iteration: {number}") # Output: 1, 2, 3, 4, 5

# Dictionary iteration
dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

for key, value in dictionary.items():
    print(f"\nDictionary iteration: {key} : {value}") # Output: 1 one, 2 two, 3 three, 4 four, 5 five

# enumerate()
skills = ["Python", "SQL", "Pandas"]

for index, skill in enumerate(skills):
    print(f"\nList comprehension: {index} : {skill}") # Output: 0 Python, 1 SQL, 2 Pandas

# zip()
names = ["Rahim", "Karim"]
marks = [85, 75]

for name, mark in zip(names, marks):
    print(f"Zip: {name} : {mark}")  # Output: Rahim : 85, Karim : 75

# 8. List Comprehension
squares = [x * x for x in range(10)]

print("\nList Comprehension: ",squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 9. Nested Data Structures
# Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nNested List: ",matrix) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested List: ",matrix[1][1]) # Output: 5

# Nested Dictionary
students = {
    "student1": {
        "name": "Jubayer",
        "age": 25,
        "courses": ["Python", "SQL"]
    },
    "student2": {
        "name": "Rahim",
        "age": 22,
        "courses": ["Python", "Machine Learning"]
    }
}

print("\nNested Dictionary: ",students) # Output: {'student1': {'name': 'Jubayer', 'age': 25, 'courses': ['Python', 'SQL']}, 'student2': {'name': 'Rahim', 'age': 22, 'courses': ['Python', 'Machine Learning']}}
print("\nNested Dictionary: ",students["student1"]["name"]) # Output: Jubayer
print("\nNested Dictionary: ",students["student2"]["courses"]) # Output: ['Python', 'Machine Learning']

# List of Tuples
people = [("Hasan", 25), ("Rahim", 22), ("Karim", 28)]

print("\nList of Tuples: ",people) # Output: [('Jubayer', 25), ('Rahim', 22), ('Karim', 28)]
print("\nList of Tuples: ",people[0]) # Output: ('Jubayer', 25)
print("\nList of Tuples: ",people[0][0]) # Output: Jubayer


# List of Dictionaries
students = [
    {"name": "Rahim", "marks": 85},
    {"name": "Karim", "marks": 75},
    {"name": "Sadia", "marks": 90}
]

for student in students:
    print(f"\nName: {student['name']}, Marks: {student['marks']}") # Output: Name: Rahim, Marks: 85, Name: Karim, Marks: 75, Name: Sadia, Marks: 90

# Dictionary of Lists
students = {
    "Rahim": [85, 90, 75],
    "Karim": [75, 80, 85],
    "Sadia": [90, 85, 95]
}

print("\nDictionary of Lists: ",students) # Output: {'Rahim': [85, 90, 75], 'Karim': [75, 80, 85], 'Sadia': [90, 85, 95]}
print("\nDictionary of Lists: ",students["Rahim"]) # Output: [85, 90, 75]
print("\nDictionary of Lists: ",students["Rahim"][0]) # Output: 85

# Dictionary of Dictionaries
students = {
    "student1": {
        "name": "Rahim",
        "marks": 85
    },
    "student2": {
        "name": "Karim",
        "marks": 75
    },
    "student3": {
        "name": "Sadia",
        "marks": 90
    }
}

print("\nDictionary of Dictionaries: ",students) # Output: {'student1': {'name': 'Rahim', 'marks': 85}, 'student2': {'name': 'Karim', 'marks': 75}, 'student3': {'name': 'Sadia', 'marks': 90}}
print("\nDictionary of Dictionaries: ",students["student1"]) # Output: {'name': 'Rahim', 'marks': 85}
print("\nDictionary of Dictionaries: ",students["student1"]["name"]) # Output: Rahim
print("\nDictionary of Dictionaries: ",students["student1"]["marks"]) # Output: 85

# 10. Dictionary & Set Comprehensions

# Square Dictionary
squares = {x: x ** 2 for x in range(1, 6)}

print("\nSquare Dictionary: ",squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Even Square Dictionary
even_squares = {x: x ** 2 for x in range(1, 6) if x % 2 == 0}

print("\nEven Square Dictionary: ",even_squares) # Output: {2: 4, 4: 16}

# Filter Dictionary
marks = {
    "Rahim": 85,
    "Karim": 45,
    "Sadia": 90
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 50
}

print("\nFilter Dictionary: ",passed) # Output: {'Rahim': 85, 'Sadia': 90}

# Unique Squares
numbers = [1, 2, 2, 3, 3, 4]

squares = {x ** 2 for x in numbers}

print("\nSet Comprehension: ",sorted(squares)) # Output: [1, 4, 9, 16]


"""
Project 01 — Student Management System

Use a list of dictionaries to implement the following features: Add, Update, Delete, Search, and Sort Students, and Calculate Average Marks.

"""

# PROJECT 01: STUDENT MANAGEMENT SYSTEM

students = [
    {"id": 1, "name": "Rahim", "marks": 85},
    {"id": 2, "name": "Karim", "marks": 75},
    {"id": 3, "name": "Sadia", "marks": 90}
]

# 1. Display Students
def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


# 2. Add Student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    new_id = max(
        (student["id"] for student in students),
        default=0
    ) + 1

    students.append({
        "id": new_id,
        "name": name,
        "marks": marks
    })

    print("Student added successfully!")


# 3. Update Student
def update_student():
    try:
        student_id = int(input("Enter student ID: "))
        new_marks = float(input("Enter new marks: "))
    except ValueError:
        print("Invalid input.")
        return

    if not 0 <= new_marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    for student in students:
        if student["id"] == student_id:
            student["marks"] = new_marks
            print("Student updated!")
            return

    print("Student not found.")


# 4. Delete Student
def delete_student():
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted!")
            return

    print("Student not found.")


# 5. Search Student
def search_student():
    name = input("Enter name to search: ").strip().lower()

    matches = [
        student for student in students
        if name in student["name"].lower()
    ] if name else []

    if matches:
        for student in matches:
            print(student)
    else:
        print("Student not found.")


# 6. Sort Students
def sort_students():
    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    for student in sorted_students:
        print(student)


# 7. Average Marks
def average_marks():
    if not students:
        print("No students available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"Average Marks: {average:.2f}")


# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Show Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Sort by Marks")
    print("7. Average Marks")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        sort_students()
    elif choice == "7":
        average_marks()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")





"""
Project 02 — Inventory Management System

Use a dictionary of lists to manage product inventory. Implement add, update, remove, search, and stock count features.

"""


# PROJECT 02: E-COMMERCE SHOPPING CART

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mouse", "price": 800},
    3: {"name": "Keyboard", "price": 1500},
    4: {"name": "Headphone", "price": 2000}
}

cart = []


# 1. Show Products
def show_products():
    print("\n===== AVAILABLE PRODUCTS =====")

    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} "
            f"- {product['price']} BDT"
        )


# 2. Add Product to Cart
def add_to_cart():
    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    if product_id not in products:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            print("Cart quantity increased!")
            return

    cart.append({
        "id": product_id,
        "name": products[product_id]["name"],
        "price": products[product_id]["price"],
        "quantity": quantity
    })

    print("Product added to cart!")


# 3. Show Cart
def show_cart():
    if not cart:
        print("Your cart is empty.")
        return

    print("\n===== YOUR CART =====")

    for item in cart:
        subtotal = item["price"] * item["quantity"]

        print(
            f"ID: {item['id']} | "
            f"{item['name']} | "
            f"Qty: {item['quantity']} | "
            f"Subtotal: {subtotal} BDT"
        )


# 4. Update Quantity
def update_quantity():
    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    for item in cart:
        if item["id"] == product_id:
            item["quantity"] = quantity
            print("Quantity updated!")
            return

    print("Product not found in cart.")


# 5. Remove Product
def remove_product():
    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Invalid product ID.")
        return

    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print("Product removed!")
            return

    print("Product not found in cart.")


# 6. Calculate Total and Discount
def calculate_total():
    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    if total >= 10000:
        discount_rate = 0.10
    elif total >= 5000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = total * discount_rate
    final_total = total - discount

    print("\n===== BILL SUMMARY =====")
    print(f"Subtotal: {total:.2f} BDT")
    print(f"Discount: {discount:.2f} BDT")
    print(f"Final Total: {final_total:.2f} BDT")


# Main Menu
while True:
    print("\n===== SHOPPING CART =====")
    print("1. Show Products")
    print("2. Add Product")
    print("3. Show Cart")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Calculate Total")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        update_quantity()
    elif choice == "5":
        remove_product()
    elif choice == "6":
        calculate_total()
    elif choice == "7":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice.")



"""
Project 03 — Simple Dataset Analyzer

Analyze a student dataset to identify missing marks and duplicate names, calculate average marks, find the highest and lowest values, and filter students who have passed.

"""


# PROJECT 03: SIMPLE DATASET ANALYZER

students = [
    {"name": "Rahim", "marks": 85},
    {"name": "Karim", "marks": 45},
    {"name": "Sadia", "marks": 90},
    {"name": "Rahim", "marks": 85},
    {"name": "Nadia", "marks": None},
    {"name": "Fahim", "marks": 70}
]

PASS_MARK = 50

print("===== DATASET ANALYZER =====")


# 1. Total Records
print("\n1. Total Records")
print("Total:", len(students))


# 2. Find Missing Marks
missing_records = [
    student for student in students
    if student["marks"] is None
]

print("\n2. Missing Marks")

for student in missing_records:
    print(student)


# 3. Find Duplicate Names
seen_names = set()
duplicate_names = set()

for student in students:
    name = student["name"].strip().lower()

    if name in seen_names:
        duplicate_names.add(name)
    else:
        seen_names.add(name)

print("\n3. Duplicate Names")
print(sorted(duplicate_names))


# 4. Remove Duplicate Records by Name
clean_students = []
seen_names = set()

for student in students:
    name = student["name"].strip().lower()

    if name not in seen_names:
        clean_students.append(student)
        seen_names.add(name)

print("\n4. After Removing Duplicates")
print("Total:", len(clean_students))


# 5. Remove Missing Marks
valid_students = [
    student for student in clean_students
    if student["marks"] is not None
]

print("\n5. Valid Records")
print("Total:", len(valid_students))


# 6. Calculate Average Marks
if valid_students:
    total = sum(
        student["marks"] for student in valid_students
    )

    average = total / len(valid_students)

    print("\n6. Average Marks")
    print(f"Average: {average:.2f}")
else:
    print("\n6. No valid marks available.")


# 7. Highest and Lowest Marks
if valid_students:
    highest = max(
        valid_students,
        key=lambda student: student["marks"]
    )

    lowest = min(
        valid_students,
        key=lambda student: student["marks"]
    )

    print("\n7. Highest Marks")
    print(highest)

    print("\n8. Lowest Marks")
    print(lowest)


# 8. Filter Passed Students
passed_students = [
    student for student in valid_students
    if student["marks"] >= PASS_MARK
]

print("\n9. Passed Students")

for student in passed_students:
    print(student)


# 9. Filter Failed Students
failed_students = [
    student for student in valid_students
    if student["marks"] < PASS_MARK
]

print("\n10. Failed Students")

for student in failed_students:
    print(student)


# 10. Final Dataset Summary
print("\n===== FINAL SUMMARY =====")
print("Original Records:", len(students))
print("Missing Marks:", len(missing_records))
print("Duplicate Names:", len(duplicate_names))
print("Clean Records:", len(valid_students))
print("Passed:", len(passed_students))
print("Failed:", len(failed_students))

if valid_students:
    print(f"Average Marks: {average:.2f}")



"""
Project 04 — Restaurant Menu & Order System

Create a restaurant menu using a dictionary of dictionaries. Implement add, update, remove, and search operations for menu items. Users should be able to add items to their order, view the order, update quantities, remove items, and calculate the total bill.

"""

# ==========================================
# PROJECT 04 - RESTAURANT MANAGEMENT SYSTEM
# ==========================================

# Dictionary of Dictionaries
menu = {
    1: {"name": "Chicken Burger", "price": 250, "category": "Fast Food"},
    2: {"name": "Chicken Pizza", "price": 650, "category": "Pizza"},
    3: {"name": "Beef Biryani", "price": 350, "category": "Rice"},
    4: {"name": "French Fries", "price": 150, "category": "Snacks"},
    5: {"name": "Cold Coffee", "price": 180, "category": "Drinks"}
}

# List of Dictionaries
orders = []


# ==========================================
# INPUT VALIDATION
# ==========================================

def get_integer(message, minimum=1):
    try:
        number = int(input(message))
        if number < minimum:
            print(f"Value must be at least {minimum}.")
            return None
        return number
    except ValueError:
        print("Invalid input! Enter a whole number.")
        return None


# ==========================================
# MENU MANAGEMENT
# ==========================================

# 1. Show Menu
def show_menu():
    print("\n========== RESTAURANT MENU ==========")

    for item_id, item in menu.items():
        print(
            f"ID: {item_id} | "
            f"{item['name']} | "
            f"Price: {item['price']} BDT | "
            f"Category: {item['category']}"
        )


# 2. Add Menu Item
def add_menu_item():
    name = input("Enter food name: ").strip()
    if not name:
        print("Food name cannot be empty.")
        return

    price = get_integer("Enter price: ")
    if price is None:
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    new_id = max(menu.keys(), default=0) + 1

    menu[new_id] = {
        "name": name,
        "price": price,
        "category": category
    }

    print("Menu item added successfully!")


# 3. Update Menu Item
def update_menu_item():
    item_id = get_integer("Enter item ID: ")
    if item_id is None:
        return

    if item_id not in menu:
        print("Item not found!")
        return

    new_name = input("Enter new name: ").strip()
    new_price = get_integer("Enter new price: ")
    if new_price is None:
        return

    new_category = input("Enter new category: ").strip()

    if not new_name or not new_category:
        print("Name and category cannot be empty.")
        return

    menu[item_id]["name"] = new_name
    menu[item_id]["price"] = new_price
    menu[item_id]["category"] = new_category

    print("Menu item updated successfully!")


# 4. Remove Menu Item
def remove_menu_item():
    item_id = get_integer("Enter item ID: ")
    if item_id is None:
        return

    if item_id in menu:
        del menu[item_id]
        print("Menu item removed successfully!")
    else:
        print("Item not found!")


# 5. Search Menu Item
def search_menu_item():
    keyword = input("Search food name: ").strip().lower()

    if not keyword:
        print("Enter a search keyword.")
        return

    found = False

    for item_id, item in menu.items():
        if keyword in item["name"].lower():
            print(item_id, item)
            found = True

    if not found:
        print("No matching food found!")


# ==========================================
# ORDER MANAGEMENT
# ==========================================

# 6. Add Food to Order
def add_order():
    show_menu()

    item_id = get_integer("Enter food ID: ")
    if item_id is None:
        return

    if item_id not in menu:
        print("Food not found!")
        return

    quantity = get_integer("Enter quantity: ")
    if quantity is None:
        return

    # Check whether food already exists in order
    for item in orders:
        if item["id"] == item_id:
            item["quantity"] += quantity
            print("Order quantity increased!")
            return

    food = menu[item_id]

    orders.append({
        "id": item_id,
        "name": food["name"],
        "price": food["price"],
        "quantity": quantity
    })

    print("Food added to order!")


# 7. View Order
def view_order():
    print("\n========== YOUR ORDER ==========")

    if not orders:
        print("No food ordered yet.")
        return

    for item in orders:
        subtotal = item["price"] * item["quantity"]

        print(
            f"ID: {item['id']} | "
            f"{item['name']} | "
            f"Qty: {item['quantity']} | "
            f"Subtotal: {subtotal} BDT"
        )


# 8. Update Order Quantity
def update_order():
    item_id = get_integer("Enter ordered food ID: ")
    if item_id is None:
        return

    quantity = get_integer("Enter new quantity: ")
    if quantity is None:
        return

    for item in orders:
        if item["id"] == item_id:
            item["quantity"] = quantity
            print("Order updated successfully!")
            return

    print("Food not found in order!")


# 9. Remove Food from Order
def remove_order():
    item_id = get_integer("Enter food ID to remove: ")
    if item_id is None:
        return

    for item in orders:
        if item["id"] == item_id:
            orders.remove(item)
            print("Food removed from order!")
            return

    print("Food not found in order!")


# 10. Calculate Bill
def calculate_bill():
    if not orders:
        print("Your order is empty!")
        return

    view_order()

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in orders
    )

    # Example VAT: 5% (configurable)
    vat_rate = 0.05
    vat = subtotal * vat_rate
    total = subtotal + vat

    print("\n========== FINAL BILL ==========")
    print(f"Subtotal: {subtotal:.2f} BDT")
    print(f"VAT (5%): {vat:.2f} BDT")
    print(f"Total Bill: {total:.2f} BDT")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n========== RESTAURANT SYSTEM ==========")
    print("1. Show Menu")
    print("2. Add Menu Item")
    print("3. Update Menu Item")
    print("4. Remove Menu Item")
    print("5. Search Menu Item")
    print("6. Add Food to Order")
    print("7. View Order")
    print("8. Update Order Quantity")
    print("9. Remove Food from Order")
    print("10. Calculate Bill")
    print("11. Exit")

    choice = input("Choose an option (1-11): ")

    if choice == "1":
        show_menu()

    elif choice == "2":
        add_menu_item()

    elif choice == "3":
        update_menu_item()

    elif choice == "4":
        remove_menu_item()

    elif choice == "5":
        search_menu_item()

    elif choice == "6":
        add_order()

    elif choice == "7":
        view_order()

    elif choice == "8":
        update_order()

    elif choice == "9":
        remove_order()

    elif choice == "10":
        calculate_bill()

    elif choice == "11":
        print("Thank you for visiting!")
        break

    else:
        print("Invalid option! Try again.")


