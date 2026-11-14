"Python Variables, input, and basic math"

name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

# Simple calculator
a = float(input("First number: "))
b = float(input("Second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b if b != 0 else "Cannot divide by zero")
print("Power:", a ** b)

#Radius
radius = float(input("Circle radius: "))
print("Area:", round(3.14159 * radius ** 2, 2))
