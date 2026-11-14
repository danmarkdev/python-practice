"for and while loops"

#Multiplication table Python
num = int(input("Table of: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Sum 1..100
total = 0
for i in range(1, 101):
    total += i
print("Sum 1-100:", total)

#FizzBuzz
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Triangle pattern
for i in range(1, 6):
    print("*" * i)

# While loop & countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
