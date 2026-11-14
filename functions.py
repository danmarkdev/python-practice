"Functions"

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def stats(*numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

print(greet("Juan"))
print(greet("Juan", "Good morning"))
print([n for n in range(1, 50) if is_prime(n)])
print("5! =", factorial(5))
print(fibonacci(10))
print(stats(3, 7, 1, 9))

#Practicing of writing gcd(a, b)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD(48, 18) =", gcd(48, 18))
