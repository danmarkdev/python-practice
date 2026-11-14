"List"

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "orange")
fruits.remove("banana")
print(fruits)
print("Sorted:", sorted(fruits))
print("Reversed:", fruits[::-1])

numbers = [4, 8, 15, 16, 23, 42]
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Max:", max(numbers), "Min:", min(numbers))

#List comprehension
squares = [n ** 2 for n in range(1, 11)]
evens = [n for n in range(1, 21) if n % 2 == 0]
print(squares)
print(evens)

#duplicates keeping order
data = [1, 2, 2, 3, 4, 4, 5, 1]
unique = []
for d in data:
    if d not in unique:
        unique.append(d)
print("Unique:", unique)

#Second Largest Number
nums = [10, 40, 20, 30, 50]
print("Second largest:", sorted(set(nums))[-2])
