# 1. Conditional Statements (if, elif, else)

# These statements control the flow of a program based on whether a condition is True or False.
# The `if` keyword starts a conditional block. The code inside an `if` block runs only if the condition is `True`.
# `elif` (short for "else if") checks another condition only if the previous `if` or `elif` conditions were `False`.
# The `else` keyword is optional. The code inside an `else` block runs if all preceding `if` and `elif` conditions are `False`.

marks = float(input("Enter your marks: "))

if marks >= 80:
    print("Grade A+")
elif marks >= 70:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail or lower grade")
    

# 2. Logical Operators (and, or, not)

# Logical operators return either `True` or `False`.
# They are used to combine multiple conditions or reverse the truth value of a condition.

# example of and operator
age = 25
has_nid = True

if age >= 18 and has_nid:
    print("Eligible")
else:
    print("Not Eligible")

# example of or operator
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")
else:
    print("Access Denied")

# example of not operator
is_logged_in = False

if not is_logged_in:
    print("Please login first")

# 3. Nested Conditional Statements 

# A nested `if` statement is an `if` inside another `if`.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("User Not Found")

# 4. For loops (The `for` loop repeats code for each item in a list, tuple, or string.)
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


prices = [100, 200, 300, 400, 500]

total = 0

for price in prices:
    total += price

print("Total Price: ", total)


# 5. While loops (A `while` loop executes code as long as a condition is `True`.)
count = 1

while count <= 5:
    print(count)
    count += 1

anotherCount = 5

while anotherCount > 0:
    print(anotherCount)
    anotherCount -= 1
    
print("Countdown Finished")

# 6. range () - generates a sequence of numbers

for number in range(5):
    print(number) # Output: 0, 1, 2, 3, 4

for number in range(1, 6):
    print(number) # Output: 1, 2, 3, 4, 5

for number in range(1, 10, 2):
    print(number) # Output: 1, 3, 5, 7, 9

# 7. break, continue, pass

# `break` exits the loop immediately.
for number in range(5):
    if number == 3:
        break
    print(number) # Output: 0, 1, 2

# `continue` skips the current iteration.
for number in range(5):
    if number == 3:
        continue
    print(number) # Output: 0, 1, 2, 4

# `pass` does nothing but satisfies syntax requirements.
for number in range(5):
    if number == 3:
        pass
    print(number) # Output: 0, 1, 2, 3, 4

# 8. Nested Loops

# Nested loops involve placing one loop inside another. The inner loop runs completely for each iteration of the outer loop.

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j) # Output:
                    # 1 1
                    # 1 2
                    # 2 1
                    # 2 2
                    # 3 1
                    # 3 2

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print() # Output:
            # * 
            # * *
            # * * *
            # * * * *
            # * * * * *


# 10. List Comprehension

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers) # Output: [1, 2, 3, 4, 5]