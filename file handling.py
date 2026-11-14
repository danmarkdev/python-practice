"Reading and writing files"

with open("notes.txt", "w") as f:
    f.write("Line one\nLine two\nLine three\n")

with open("notes.txt", "a") as f:
    f.write("Line four\n")

with open("notes.txt", "r") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())

#Count lines & words
with open("notes.txt") as f:
    content = f.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))

#Save & load a list
import json
data = {"students": ["Ana", "Ben", "Cara"], "passed": 3}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json") as f:
    print(json.load(f))
