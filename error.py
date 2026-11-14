"error handling"

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again.")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
age = get_number("Enter your age: ")
print("You entered:", age)

try:
    open("missing_file.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done.")
