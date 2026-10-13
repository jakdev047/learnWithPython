"""
1. Python Fundamentals
    Comments
    Variables
    Data Types
    Type Casting
    Input
    Output
    Operators
    f-strings
"""
# syntax
print("Hello World!")

# variable (int, str, float, bool)
userName = "Jubayer Alam Khan"
quantity= 10
price = 150.50
isBuy = True

print("isBuy: ",isBuy)

# type of variable
print("type of userName: ",type(userName))
print("type of quantity: ",type(quantity))
print("type of price: ",type(price))
print("type of isBuy: ",type(isBuy))

# f-string
print(f"My name is {userName} and I have {quantity} items in my cart at {price} TK.")

# type casting str(), int(), float(), bool()
quantity = str(quantity)
print("type of quantity: ",type(quantity))

# input (str)
userEmail= input("Enter your email: ")
print("userEmail: ",userEmail)


# Operators (Arithmetic, Comparison, Logical, Assignment, Identity, Membership, Bitwise)
# Arithmetic (+, -, *, /, %, //, **)
num1 = 10
num2 = 3
numbers = [10, 20, 30, 40, 50]

print("num1 + num2: ",num1 + num2) # add [Result: 13]
print("num1 - num2: ",num1 - num2) # substact [Result: 7]
print("num1 * num2: ",num1 * num2) # multiply [Result: 30]
print("num1 / num2: ",num1 / num2) # divide [Result: 3.3333333333333335]
print("num1 % num2: ",num1 % num2) # modulo [Result: 1]
print("num1 // num2: ",num1 // num2) # floor divide [Result: 3]
print("num1 ** num2: ",num1 ** num2) # exponential [Result: 1000]

# Comparison (==, !=, >, <, >=, <=)
print("num1 == num2: ",num1 == num2) # equal [Result: False]
print("num1 != num2: ",num1 != num2) # not equal [Result: True]
print("num1 > num2: ",num1 > num2) # greater than [Result: True]
print("num1 < num2: ",num1 < num2) # less than [Result: False]
print("num1 >= num2: ",num1 >= num2) # greater than or equal to [Result: True]
print("num1 <= num2: ",num1 <= num2) # less than or equal to [Result: False]

# Logical (and, or, not)
print("num1 and num2: ",num1 and num2) # logical and [Result: 10]
print("num1 or num2: ",num1 or num2) # logical or [Result: 10]
print("not num1: ",not num1) # logical not [Result: False]
print("not num2: ",not num2) # logical not [Result: False]

# Assignment (=, +=, -=, *=, /=, %=, //=, **=)
num1 += num2
print("num1 += num2:", num1)  # Add and assign [Result: 13]

num1 -= num2
print("num1 -= num2:", num1)  # Subtract and assign [Result: 7]

num1 *= num2
print("num1 *= num2:", num1)  # Multiply and assign [Result: 21]

num1 /= num2
print("num1 /= num2:", num1)  # Divide and assign [Result: 7.0]

num1 %= num2
print("num1 %= num2:", num1)  # Modulo and assign [Result: 1.0]

num1 //= num2
print("num1 //= num2:", num1)  # Floor divide and assign [Result: 1.0]

num1 **= num2
print("num1 **= num2:", num1)  # Exponential and assign [Result: 1.0]

# Identity (is, is not)
print("num1 is num2: ",num1 is num2) # check if same object [Result: False]
print("num1 is not num2: ",num1 is not num2) # check if not same object [Result: True]

# Membership (in, not in)
print("num1 in num2: ",num1 in numbers) # check if member [Result: False]
print("num1 not in num2: ",num1 not in numbers) # check if not member [Result: True]

# Bitwise (&, |, ^, ~, <<, >>) bin()
print("num1 & num2: ",int(num1) & num2) # bitwise and [Result: 0]
print("num1 | num2: ",int(num1) | num2) # bitwise or [Result: 1]
print("num1 ^ num2: ",int(num1) ^ num2) # bitwise xor [Result: 1]
print("num1 ~ num2: ",~int(num1)) # bitwise not [Result: -1] (~n = -(n+1))
print("num1 << num2: ",int(num1) << num2) # bitwise left shift [Result: 4] (n << m = n * (2**m))
print("num1 >> num2: ",int(num1) >> num2) # bitwise right shift [Result: 0] (n >> m = n // (2**m))


# Practice: Get user information

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Hello {name}")
print(f"Your BMI is {bmi:.2f}")