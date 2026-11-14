"Dictionaries and sets"

student = {"name": "Maria", "age": 20, "course": "BSED"}
student["grade"] = 92
for key, value in student.items():
    print(key, ":", value)

#Word counter
sentence = "the quick brown fox jumps over the lazy dog the end"
counts = {}
for w in sentence.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)
most = max(counts, key=counts.get)
print("Most common:", most, counts[most])

#Phonebook
phonebook = {}
phonebook["Ana"] = "0917-111-2222"
phonebook["Ben"] = "0918-333-4444"
print(phonebook.get("Ana", "Not found"))
print(phonebook.get("Zed", "Not found"))

#Sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
