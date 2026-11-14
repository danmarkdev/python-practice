"Strings"

text = input("Enter a sentence: ")
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Length:", len(text))
print("Words:", len(text.split()))
print("Reversed:", text[::-1])

# Palindrome check
word = input("Enter a word: ").lower()
print("Palindrome!" if word == word[::-1] else "Not a palindrome")

# Count vowels
vowels = sum(1 for ch in text.lower() if ch in "aeiou")
print("Vowels:", vowels)

# Character frequency
freq = {}
for ch in text.replace(" ", "").lower():
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Caesar cipher
def caesar(msg, shift):
    out = ""
    for ch in msg:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out

secret = caesar("Hello World", 3)
print(secret, "->", caesar(secret, -3))
