"if / elif / else"

# Grade checker
score = int(input("Enter your score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade:", grade)

# Even or odd
n = int(input("Enter a number: "))
print(n, "is", "even" if n % 2 == 0 else "odd")

# Leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# PRACTICE: find the largest of 3 numbers
x, y, z = 10, 25, 17
print("Largest:", max(x, y, z))
