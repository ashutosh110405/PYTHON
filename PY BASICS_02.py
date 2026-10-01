"""
================================================================================
       PYTHON BASICS PART 2: USER INPUT, CONTROL FLOW, LOOPS & FUNCTIONS
================================================================================
Covers everything not in Part 1:
  1. User Input (Single, Type-casted, Multiple inputs in one line)
  2. Decision Making (if, elif, else, ternary operator, match-case)
  3. Loops (for, while, range, break, continue, pass, loop-else)
  4. String Slicing & Important Methods
  5. List & Dictionary Operations + Comprehensions
  6. Functions (def, return, default args, *args, **kwargs, lambda)
  7. Exception Handling (try, except, else, finally)
================================================================================
Tip: You can type your own input, or just press [ENTER] to use default values!
================================================================================
"""

# ==============================================================================
# 1. USER INPUT TECHNIQUES
# ==============================================================================
print("=" * 60)
print(" 1. USER INPUT TECHNIQUES ")
print("=" * 60)

# input() always returns data as a string (str).
# You must cast (convert) it to int or float for math.

# 1.1 Simple string input
name = input("Enter your name [Default: Ashutosh]: ").strip() or "Ashutosh"
print(f"Hello, {name}!")

# 1.2 Integer input with type casting
age_str = input("Enter your age [Default: 22]: ").strip() or "22"
age = int(age_str)  # Cast to integer
print(f"Next year you will be: {age + 1} years old.")

# 1.3 Float input
height_str = input("Enter your height in feet [Default: 5.9]: ").strip() or "5.9"
height = float(height_str)  # Cast to float
print(f"Height in inches: {height * 12:.1f} inches.")

# 1.4 Taking multiple inputs in ONE line using split()
nums_str = input("Enter 3 space-separated numbers [Default: 10 20 30]: ").strip() or "10 20 30"
n1, n2, n3 = map(int, nums_str.split())
print(f"You entered: n1={n1}, n2={n2}, n3={n3} | Sum = {n1 + n2 + n3}")


# ==============================================================================
# 2. DECISION MAKING (CONDITIONALS)
# ==============================================================================
print("\n" + "=" * 60)
print(" 2. DECISION MAKING (IF - ELIF - ELSE) ")
print("=" * 60)

score_str = input("Enter your test marks (0-100) [Default: 85]: ").strip() or "85"
score = int(score_str)

# 2.1 Standard if - elif - else
if score >= 90:
    grade = "A+"
elif score >= 75:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Score: {score} -> Grade: {grade}")

# 2.2 Ternary Operator (One-line if-else)
# Syntax: [value_if_true] if [condition] else [value_if_false]
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} -> Status: {status}")

# 2.3 Match-Case (Python 3.10+ Pattern Matching, similar to switch-case)
choice = input("Enter a day number (1-3) [Default: 1]: ").strip() or "1"
match choice:
    case "1":
        print("Day 1: Monday")
    case "2":
        print("Day 2: Tuesday")
    case "3":
        print("Day 3: Wednesday")
    case _:
        print("Other day")


# ==============================================================================
# 3. LOOPS & ITERATIONS
# ==============================================================================
print("\n" + "=" * 60)
print(" 3. LOOPS & ITERATION ")
print("=" * 60)

count_str = input("Enter a number to print multiplication table [Default: 5]: ").strip() or "5"
num = int(count_str)

# 3.1 For Loop with range(start, stop, step)
print(f"\nMultiplication Table for {num}:")
for i in range(1, 6):  # 1 to 5
    print(f"  {num} x {i} = {num * i}")

# 3.2 While Loop
print("\nCountdown using while loop:")
counter = 3
while counter > 0:
    print(f"  Counting: {counter}")
    counter -= 1

# 3.3 Loop Controls: break, continue, pass
print("\nBreak and Continue Demo (range 1 to 6):")
for i in range(1, 7):
    if i == 2:
        print(f"  Skipping {i} with 'continue'")
        continue  # Skips rest of current iteration
    if i == 5:
        print(f"  Stopping loop at {i} with 'break'")
        break     # Terminates loop completely
    print(f"  Current value: {i}")

# 3.4 For-Else (Else executes only if loop finishes WITHOUT a break)
print("\nFor-Else Demo:")
for i in [1, 2, 3]:
    pass  # 'pass' does nothing (placeholder)
else:
    print("  Loop finished normally without hitting 'break'!")


# ==============================================================================
# 4. STRING SLICING & USEFUL METHODS
# ==============================================================================
print("\n" + "=" * 60)
print(" 4. STRING SLICING & METHODS ")
print("=" * 60)

user_word = input("Enter a word to test slicing [Default: Python]: ").strip() or "Python"

# String indexing & slicing: string[start : stop : step]
print(f"Original word : {user_word}")
print(f"First character [0]   : {user_word[0]}")
print(f"Last character  [-1]  : {user_word[-1]}")
print(f"First 3 chars   [:3]  : {user_word[:3]}")
print(f"Reversed string [::-1]: {user_word[::-1]}")

# Palindrome Check task
is_palindrome = user_word.lower() == user_word[::-1].lower()
print(f"Is '{user_word}' a palindrome? -> {is_palindrome}")

# Useful string methods
sample_txt = "  python programming is fun  "
print(f"strip()   : '{sample_txt.strip()}' (removes extra spaces)")
print(f"upper()   : '{sample_txt.strip().upper()}'")
print(f"replace() : '{sample_txt.strip().replace('fun', 'awesome')}'")
print(f"split()   : {sample_txt.strip().split()} (splits into list of words)")


# ==============================================================================
# 5. LIST & DICTIONARY OPERATIONS + COMPREHENSIONS
# ==============================================================================
print("\n" + "=" * 60)
print(" 5. LISTS, DICTS & COMPREHENSIONS ")
print("=" * 60)

# List methods
items = [10, 20, 30]
items.append(40)       # Add at the end
items.insert(1, 15)    # Insert 15 at index 1
removed_item = items.pop()  # Removes last item
print(f"Updated list: {items} | Popped item: {removed_item}")

# List Comprehension: Quick way to create lists
# Task: Create a list of squares of numbers from 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares (1 to 5): {squares}")

# Filter even numbers using comprehension
evens = [x for x in [1, 2, 3, 4, 5, 6, 7, 8] if x % 2 == 0]
print(f"Even numbers filtered: {evens}")

# Dictionary methods
person = {"name": name, "age": age, "role": "Developer"}
print(f"Dict keys   : {list(person.keys())}")
print(f"Dict values : {list(person.values())}")
print(f"get() method: {person.get('role', 'Not Found')}")  # Safe access


# ==============================================================================
# 6. FUNCTIONS & LAMBDA
# ==============================================================================
print("\n" + "=" * 60)
print(" 6. FUNCTIONS & LAMBDA ")
print("=" * 60)

# 6.1 Function with default argument & return value
def calculate_total(price, tax_rate=0.05):
    """Calculates final price with tax."""
    return price + (price * tax_rate)

final_price = calculate_total(100)
print(f"calculate_total(100) with default 5% tax = {final_price}")

# 6.2 Returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 12, 1, 99, 23])
print(f"Multiple returns: Min = {low}, Max = {high}")

# 6.3 *args (Variable number of positional arguments)
def sum_all(*args):
    return sum(args)

print(f"*args demo (sum 1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

# 6.4 **kwargs (Variable number of keyword arguments)
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("kwargs demo:")
show_profile(city="Pune", college="MES IMCC", stream="MCA")

# 6.5 Lambda (Anonymous 1-line function)
# Syntax: lambda arguments : expression
multiply = lambda x, y: x * y
print(f"Lambda multiplication (4 * 5) = {multiply(4, 5)}")


# ==============================================================================
# 7. EXCEPTION HANDLING (TRY - EXCEPT - ELSE - FINALLY)
# ==============================================================================
print("\n" + "=" * 60)
print(" 7. EXCEPTION HANDLING ")
print("=" * 60)
# Handles runtime errors safely without crashing the program

test_input = input("Enter a number to divide 100 by [Default: 20]: ").strip() or "20"

try:
    divisor = int(test_input)
    result = 100 / divisor
except ValueError:
    print("Error: Invalid input! You must enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    # Runs ONLY if no error occurred
    print(f"Success! 100 / {divisor} = {result}")
finally:
    # ALWAYS runs, no matter what
    print("Finally block: Execution completed safely.")

print("\n" + "=" * 60)
print(" ALL TOPICS COMPLETED SUCCESSFULLY! ")
print("=" * 60)
