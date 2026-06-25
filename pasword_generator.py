import random

print ("länge des passwortes:")
length = int(input())

while length < 8:
    print("Passwort zu kurz")
    length = int(input("Bitte geben Sie eine gültige Länge ein: "))
else:
    print("Passwort ist okay")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
digits = "1234567890"

categories = [letters, symbols, digits]
category_counts = [length // len(categories)] * len(categories) 

for i in range(length % len(categories)):
    category_counts[i] += 1

password_chars = []
for count, chars in zip(category_counts, categories):
    password_chars.extend(random.choice(chars) for _ in range(count))

random.shuffle(password_chars)
password = "".join(password_chars)
print("Generiertes Passwort:", password)

print("Möchten Sie das Passwort in einer Datei speichern? (ja/nein)")