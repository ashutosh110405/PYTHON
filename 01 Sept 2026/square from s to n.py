#accept 2 value s and n square of n numbrt starting from s.
s = int(input("Enter the starting value: "))
n = int(input("Enter the number of squares to calculate: "))
for i in range(n):
    square = (s + i) ** 2
    print(f"Square of {s + i} is: {square}")