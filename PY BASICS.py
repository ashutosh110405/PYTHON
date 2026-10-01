"""
================================================================================
           PYTHON FUNDAMENTALS & OPERATORS: SHORT & EASY GUIDE
================================================================================
Simple, concise notes with short comments, clear examples, and exact outputs.
================================================================================
"""

# ==============================================================================
# PART 1: PYTHON FUNDAMENTALS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. COMMENTS
# ------------------------------------------------------------------------------
# 1. Single-line comment: Starts with '#'
x = 10  # This is an inline comment

# 2. Multi-line comment: Triple quotes (''' or \"\"\") not assigned to a variable
'''
This is a multi-line comment.
Used for longer notes.
'''

# 3. Docstring: Placed inside functions/classes to document them
def greet():
    """Returns a welcome message."""
    return "Hello!"

print("--- 1. Comments ---")
print("Docstring:", greet.__doc__)
# Output: Docstring: Returns a welcome message.


# ------------------------------------------------------------------------------
# 2. VARIABLES & DYNAMIC TYPING
# ------------------------------------------------------------------------------
# Variables store data. No type declaration needed (Dynamic Typing).
# Rules: Must start with a letter or '_', cannot start with a number.

name = "Ashutosh"  # String
age = 22           # Integer
height = 5.9       # Float
is_student = True  # Boolean

print("\n--- 2. Variables ---")
print(name, type(name))        # Output: Ashutosh <class 'str'>
print(age, type(age))          # Output: 22 <class 'int'>

# Dynamic Typing: Same variable can hold different types
var = 10           # Starts as int
var = "Now text"   # Changed to str
print("Dynamic var:", var)     # Output: Dynamic var: Now text

# Multiple assignment
a, b, c = 1, 2, 3
print("Multiple assignment:", a, b, c)  # Output: Multiple assignment: 1 2 3


# ------------------------------------------------------------------------------
# 3. BUILT-IN DATA TYPES
# ------------------------------------------------------------------------------
print("\n--- 3. Data Types ---")

# 1. Numbers: int, float, complex
n1 = 25          # int: whole numbers
n2 = 3.14        # float: decimal numbers
n3 = 2 + 3j      # complex: real + imaginary part
print("Numbers:", n1, n2, n3)

# 2. String (str): Text enclosed in quotes (immutable)
msg = "Python"
print("String:", msg, "| Length:", len(msg))

# 3. List: Ordered, changeable (mutable), allows duplicates
my_list = [10, 20, "apple", True]
my_list[0] = 99  # Allowed (mutable)
print("List:", my_list)

# 4. Tuple: Ordered, unchangeable (immutable), allows duplicates
my_tuple = (10, 20, 30)
# my_tuple[0] = 99  # Error! Cannot change tuples
print("Tuple:", my_tuple)

# 5. Dictionary (dict): Key-value pairs (keys must be unique)
my_dict = {"name": "Ashutosh", "roll": 101}
print("Dict:", my_dict, "| Name:", my_dict["name"])

# 6. Set: Unordered, unique items (removes duplicates automatically)
my_set = {1, 2, 2, 3, 4, 4}
print("Set (no duplicates):", my_set)

# 7. Boolean (bool): True or False
is_valid = True
print("Boolean:", is_valid)

# 8. NoneType: Represents absence of value
empty_val = None
print("NoneType:", empty_val)


# ------------------------------------------------------------------------------
# 4. TYPE CASTING (CONVERSION)
# ------------------------------------------------------------------------------
print("\n--- 4. Type Casting ---")

# Implicit: Done automatically (e.g., int + float -> float)
res = 10 + 2.5
print("Implicit (10 + 2.5):", res, type(res))  # Output: 12.5 <class 'float'>

# Explicit: Converted manually using functions
s = "100"
num = int(s)         # str -> int
flt = float(s)       # str -> float
txt = str(250)       # int -> str
lst = list("ABC")    # str -> list of chars
print("int('100')   :", num, type(num))
print("float('100') :", flt, type(flt))
print("str(250)     :", txt, type(txt))
print("list('ABC')  :", lst)


# ------------------------------------------------------------------------------
# 5. INPUT & OUTPUT (I/O)
# ------------------------------------------------------------------------------
print("\n--- 5. Input & Output ---")

# print() with 'sep' (separator) and 'end'
print("A", "B", "C", sep="-")                # Output: A-B-C
print("Hello", end=" ")                      # Output: Hello World (on same line)
print("World")

# f-strings: Best way to format output
user = "Ashutosh"
score = 95.5
print(f"User: {user}, Score: {score}")       # Output: User: Ashutosh, Score: 95.5

# input() reads string from user (commented out for smooth run)
# user_input = input("Enter something: ")


# ==============================================================================
# PART 2: PYTHON OPERATORS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ARITHMETIC OPERATORS (Math calculations)
# ------------------------------------------------------------------------------
print("\n--- 1. Arithmetic Operators ---")
p, q = 15, 4

print("Addition (+)       : 15 + 4  =", p + q)    # 19
print("Subtraction (-)    : 15 - 4  =", p - q)    # 11
print("Multiplication (*) : 15 * 4  =", p * q)    # 60
print("True Division (/)  : 15 / 4  =", p / q)    # 3.75 (always returns float)
print("Floor Division (//): 15 // 4 =", p // q)   # 3 (quotient without decimals)
print("Modulus (%)        : 15 % 4  =", p % q)    # 3 (remainder of division)
print("Exponentiation (**): 2 ** 3  =", 2 ** 3)   # 8 (2 to the power 3)


# ------------------------------------------------------------------------------
# 2. COMPARISON OPERATORS (Return True or False)
# ------------------------------------------------------------------------------
print("\n--- 2. Comparison Operators ---")
x, y = 20, 10

print("Equal to (==)                 : 20 == 10 ->", x == y)  # False
print("Not equal to (!=)             : 20 != 10 ->", x != y)  # True
print("Greater than (>)              : 20 > 10  ->", x > y)   # True
print("Less than (<)                 : 20 < 10  ->", x < y)   # False
print("Greater than or equal to (>=) : 20 >= 10 ->", x >= y)  # True
print("Less than or equal to (<=)    : 20 <= 10 ->", x <= y)  # False

# Chained comparison
print("Chained (5 < 10 < 15)         :", 5 < 10 < 15)         # True


# ------------------------------------------------------------------------------
# 3. ASSIGNMENT OPERATORS (Assign or update values)
# ------------------------------------------------------------------------------
print("\n--- 3. Assignment Operators ---")
val = 10
print("Initial val   =", val)

val += 5   # val = val + 5
print("val += 5  ->", val)  # 15

val -= 3   # val = val - 3
print("val -= 3  ->", val)  # 12

val *= 2   # val = val * 2
print("val *= 2  ->", val)  # 24

val /= 4   # val = val / 4
print("val /= 4  ->", val)  # 6.0

val //= 2  # val = val // 2
print("val //= 2 ->", val)  # 3.0

val **= 2  # val = val ** 2
print("val **= 2 ->", val)  # 9.0

val %= 4   # val = val % 4
print("val %= 4  ->", val)  # 1.0

# Walrus Operator (:=) -> Assigns value inside an expression (Python 3.8+)
if (n := len("Python")) > 3:
    print(f"Walrus (:=) length is {n}")  # Output: Walrus (:=) length is 6


# ------------------------------------------------------------------------------
# 4. LOGICAL OPERATORS (Combine conditions)
# ------------------------------------------------------------------------------
print("\n--- 4. Logical Operators ---")
# and : True only if BOTH conditions are True
# or  : True if AT LEAST ONE condition is True
# not : Inverts result (True becomes False, False becomes True)

print("True and False :", True and False)  # False
print("True and True  :", True and True)   # True
print("True or False  :", True or False)   # True
print("False or False :", False or False) # False
print("not True       :", not True)        # False
print("not False      :", not False)       # True


# ------------------------------------------------------------------------------
# 5. BITWISE OPERATORS (Operate on binary bits: 0 and 1)
# ------------------------------------------------------------------------------
print("\n--- 5. Bitwise Operators ---")
# 6 in binary = 0110
# 3 in binary = 0011

b1, b2 = 6, 3
print("b1 = 6 (0110), b2 = 3 (0011)")
print("AND (&)        : 6 & 3  =", b1 & b2)   # 0010 -> 2
print("OR (|)         : 6 | 3  =", b1 | b2)   # 0111 -> 7
print("XOR (^)        : 6 ^ 3  =", b1 ^ b2)   # 0101 -> 5 (different bits = 1)
print("NOT (~)        : ~6     =", ~b1)       # -(x + 1) -> -7
print("Left Shift (<<): 6 << 1 =", b1 << 1)   # 6 * 2 = 12
print("Right Shift(>>): 6 >> 1 =", b1 >> 1)   # 6 // 2 = 3


# ------------------------------------------------------------------------------
# 6. IDENTITY OPERATORS (Check if both point to same memory location)
# ------------------------------------------------------------------------------
print("\n--- 6. Identity Operators ---")
# is     : True if both variables are the exact SAME object in memory
# is not : True if both variables are DIFFERENT objects

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 (Same values?)  :", list1 == list2)  # True
print("list1 is list2 (Same memory?)  :", list1 is list2)  # False (different objects)
print("list1 is list3 (Same memory?)  :", list1 is list3)  # True (list3 points to list1)
print("list1 is not list2             :", list1 is not list2)  # True


# ------------------------------------------------------------------------------
# 7. MEMBERSHIP OPERATORS (Check if item exists in sequence)
# ------------------------------------------------------------------------------
print("\n--- 7. Membership Operators ---")
# in     : True if item is present
# not in : True if item is NOT present

fruits = ["apple", "banana", "mango"]

print("'banana' in fruits     :", "banana" in fruits)      # True
print("'grapes' in fruits     :", "grapes" in fruits)      # False
print("'grapes' not in fruits :", "grapes" not in fruits)  # True

text = "Python Programming"
print("'Python' in text       :", "Python" in text)        # True


# ------------------------------------------------------------------------------
# 8. OPERATOR PRECEDENCE (Execution Order)
# ------------------------------------------------------------------------------
print("\n--- 8. Operator Precedence ---")
# Order: () -> ** -> (*, /, //, %) -> (+, -) -> Comparisons -> not -> and -> or

# Example: 10 + 2 * 3 ** 2
# Step 1: 3 ** 2 = 9
# Step 2: 2 * 9  = 18
# Step 3: 10 + 18 = 28
res_order = 10 + 2 * 3 ** 2
print("10 + 2 * 3 ** 2 =", res_order)  # 28

# Using parentheses () to force order:
print("(10 + 2) * 3    =", (10 + 2) * 3)  # 36

print("\n" + "=" * 50)
print(" Done! All Fundamentals & Operators Covered ")
print("=" * 50)
