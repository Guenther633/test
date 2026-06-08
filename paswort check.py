password = input("Gib dein Passwort ein: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%&?*"


for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

has_length = len(password) >= 8
score = sum([has_upper, has_lower, has_digit, has_special, has_length])

if score >= 5:
    strength = "Stark"
elif score >= 3:
    strength = "Mittel"
else:
    strength = "Schwach"

print(f"Dein Passwort ist: {strength}")

if not has_upper:
    print("Es fehlt ein Großbuchstabe.")
if not has_lower:
    print("Es fehlt ein Kleinbuchstabe.")
if not has_digit:
    print("Es fehlt eine Zahl.")
if not has_special:
    print("Es fehlt ein Sonderzeichen.")
if not has_length:
    print("Das Passwort ist zu kurz (mind. 8 Zeichen).")
if score >= 5:
    print("Gut gemacht! Dein Passwort ist stark.")